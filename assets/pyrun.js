/* Shared Python runner: window.PyRun. One Pyodide worker per page, started on first use.
   Config (set before loading, optional): window.PYRUN = {base:'/playground/', data:false, packages:[]}  */
(function () {
  var cfg = Object.assign({ base: '/playground/', data: false, packages: [] }, window.PYRUN || {});
  var w, seq = 0, pending = {}, bufs = {}, listeners = [], state = 'idle', readyP;
  function emit(m) { listeners.forEach(function (f) { f(m); }); }
  function start() {
    if (w) return readyP;
    w = new Worker('/assets/pyworker.js');
    readyP = new Promise(function (res, rej) {
      w.onmessage = function (e) {
        var m = e.data;
        if (m.type === 'ready') { state = 'ready'; res(m); emit(m); }
        else if (m.type === 'fatal') { state = 'fatal'; rej(new Error(m.message)); emit(m); }
        else if (m.type === 'out') { bufs[m.id] = (bufs[m.id] || '') + (m.err ? '\u0001' + m.text + '\u0002' : m.text); }
        else if (m.type === 'result') { var p = pending[m.id]; if (p) { delete pending[m.id]; m.out = bufs[m.id] || ''; delete bufs[m.id]; p(m); } }
        else if (m.type === 'reset-done') { var q = pending[m.id]; if (q) { delete pending[m.id]; q(m); } }
        else emit(m);
      };
      w.postMessage({ type: 'init', base: cfg.base, data: cfg.data, packages: cfg.packages });
    });
    state = 'starting';
    return readyP;
  }
  function call(msg) {
    return start().then(function () {
      return new Promise(function (res) { var id = ++seq; pending[id] = res; msg.id = id; w.postMessage(msg); });
    });
  }
  window.PyRun = {
    start: start,
    run: function (code, fresh) { return call({ type: 'run', code: code, fresh: !!fresh }); },
    reset: function () { return call({ type: 'reset' }); },
    on: function (f) { listeners.push(f); },
    state: function () { return state; }
  };
})();
