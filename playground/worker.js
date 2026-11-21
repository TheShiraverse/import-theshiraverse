// Pyodide runs here, off the main thread, so a slow cell never freezes the page.
importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js');

let py, manifest;
const post = (m) => self.postMessage(m);

const HELPER = `
import ast, traceback, sys, warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
_g = {"__name__": "__main__"}
def _run(code):
    try:
        tree = ast.parse(code, mode="exec")
        last = None
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            last = ast.Expression(tree.body.pop().value)
        exec(compile(tree, "<cell>", "exec"), _g)
        val = eval(compile(last, "<cell>", "eval"), _g) if last is not None else None
    except BaseException as e:
        tb = e.__traceback__.tb_next
        return {"error": "".join(traceback.format_exception(type(e), e, tb)).rstrip()}
    if val is None:
        return {}
    if hasattr(val, "_repr_html_"):
        try:
            h = val._repr_html_()
            if h: return {"html": h}
        except Exception:
            pass
    return {"text": repr(val)}
`;

async function init() {
  post({ type: 'progress', msg: 'Starting Python (one-time download, about 10 MB)...' });
  py = await loadPyodide();
  post({ type: 'progress', msg: 'Loading pandas and NumPy...' });
  await py.loadPackage(['pandas', 'numpy']);
  py.setStdout({ batched: (s) => post({ type: 'out', text: s + '\n' }) });
  py.setStderr({ batched: (s) => post({ type: 'out', text: s + '\n', err: true }) });
  py.runPython(HELPER);
  post({ type: 'progress', msg: 'Downloading the RetailMart starter tables...' });
  manifest = await (await fetch('manifest.json')).json();
  py.FS.mkdirTree('/home/pyodide/data');
  for (const t of manifest.tables) {
    const res = await fetch('data/' + t.file + '.gz');
    if (!res.ok) throw new Error('Could not download ' + t.file + ' (' + res.status + ')');
    const stream = res.body.pipeThrough(new DecompressionStream('gzip'));
    const buf = new Uint8Array(await new Response(stream).arrayBuffer());
    py.FS.writeFile('/home/pyodide/data/' + t.file, buf);
  }
  post({ type: 'ready', tables: manifest.tables.map((t) => ({ file: t.file, rows: t.rows, cols: t.cols })) });
}

const ready = init();
ready.catch((e) => post({ type: 'fatal', message: String((e && e.message) || e) }));

self.onmessage = async (e) => {
  const { type, id, code } = e.data;
  if (type !== 'run') return;
  try {
    await ready;
    const t0 = performance.now();
    const r = py.globals.get('_run')(code).toJs({ dict_converter: Object.fromEntries });
    post({ type: 'result', id, ms: performance.now() - t0, ...r });
  } catch (err) {
    post({ type: 'result', id, error: String((err && err.message) || err) });
  }
};
