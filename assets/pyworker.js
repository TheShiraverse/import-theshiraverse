// Shared Pyodide worker for the playground and every Nukte deck.
// First message: {type:'init', base:'/playground/', data:true|false, packages:['pandas','numpy']}
importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js');

let py, ready, curId = 0;
const post = (m) => self.postMessage(m);

const HELPER = `
import ast, traceback, sys, warnings, types
warnings.filterwarnings('ignore', category=DeprecationWarning)
_g = {"__name__": "__main__"}
def _vars():
    out = []
    for k, v in _g.items():
        if k.startswith('_') or isinstance(v, types.ModuleType):
            continue
        r = repr(v)
        if len(r) > 60: r = r[:57] + '...'
        out.append([k, type(v).__name__, r])
    return out
def _run(code, fresh=False):
    res = {}
    if fresh: _reset()
    try:
        tree = ast.parse(code, mode="exec")
        last = None
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            last = ast.Expression(tree.body.pop().value)
        exec(compile(tree, "<cell>", "exec"), _g)
        val = eval(compile(last, "<cell>", "eval"), _g) if last is not None else None
        if val is not None:
            h = None
            if hasattr(val, "_repr_html_"):
                try: h = val._repr_html_()
                except Exception: h = None
            if h: res["html"] = h
            else: res["text"] = repr(val)
    except BaseException as e:
        tb = e.__traceback__.tb_next
        res["error"] = "".join(traceback.format_exception(type(e), e, tb)).rstrip()
    res["vars"] = _vars()
    return res
def _reset():
    _g.clear(); _g["__name__"] = "__main__"
`;

async function init(cfg) {
  post({ type: 'progress', msg: 'Starting Python (one-time download, about 10 MB)...' });
  py = await loadPyodide();
  const pk = cfg.packages || [];
  if (pk.length) {
    post({ type: 'progress', msg: 'Loading ' + pk.join(' and ') + '...' });
    await py.loadPackage(pk);
  }
  py.setStdout({ batched: (s) => post({ type: 'out', id: curId, text: s + '\n' }) });
  py.setStderr({ batched: (s) => post({ type: 'out', id: curId, text: s + '\n', err: true }) });
  py.runPython(HELPER);
  let tables = [];
  if (cfg.data) {
    post({ type: 'progress', msg: 'Downloading the RetailMart starter tables...' });
    const manifest = await (await fetch(cfg.base + 'manifest.json')).json();
    py.FS.mkdirTree('/home/pyodide/data');
    for (const t of manifest.tables) {
      const res = await fetch(cfg.base + 'data/' + t.file + '.gz');
      if (!res.ok) throw new Error('Could not download ' + t.file + ' (' + res.status + ')');
      const stream = res.body.pipeThrough(new DecompressionStream('gzip'));
      py.FS.writeFile('/home/pyodide/data/' + t.file, new Uint8Array(await new Response(stream).arrayBuffer()));
    }
    tables = manifest.tables.map((t) => ({ file: t.file, rows: t.rows, cols: t.cols }));
  }
  post({ type: 'ready', tables });
}

self.onmessage = async (e) => {
  const m = e.data;
  if (m.type === 'init') {
    ready = init(m);
    ready.catch((err) => post({ type: 'fatal', message: String((err && err.message) || err) }));
    return;
  }
  if (!ready) return;
  try {
    await ready;
    if (m.type === 'reset') { py.globals.get('_reset')(); post({ type: 'reset-done', id: m.id }); return; }
    if (m.type !== 'run') return;
    curId = m.id;
    const t0 = performance.now();
    const r = py.globals.get('_run')(m.code, !!m.fresh).toJs({ dict_converter: Object.fromEntries });
    post({ type: 'result', id: m.id, ms: performance.now() - t0, ...r });
  } catch (err) {
    post({ type: 'result', id: m.id, error: String((err && err.message) || err), vars: [] });
  }
};
