(function () {
  var scenes = [].slice.call(document.querySelectorAll('.scene'));
  var cur = 0, prog = document.querySelector('.progress'), foot = document.getElementById('footinfo');
  function esc(s) { return String(s).replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); }
  function show(i, noHash) {
    i = Math.max(0, Math.min(scenes.length - 1, i));
    scenes.forEach(function (s, k) { s.classList.toggle('active', k === i); });
    cur = i;
    scenes[i].scrollTop = 0;
    prog.style.width = ((i + 1) / scenes.length * 100) + '%';
    foot.innerHTML = '<b>' + (i + 1) + ' / ' + scenes.length + '</b> &middot; ' + esc(scenes[i].getAttribute('data-title') || '');
    if (!noHash) { try { history.replaceState(null, '', '#' + (i + 1)); } catch (e) {} }
  }
  var from = parseInt((location.hash || '').slice(1), 10);
  show(isNaN(from) ? 0 : from - 1, true);
  document.getElementById('prev').onclick = function () { show(cur - 1); };
  document.getElementById('next').onclick = function () { show(cur + 1); };
  var menu = document.getElementById('menu');
  menu.querySelector('ol').innerHTML = scenes.map(function (s, k) { return '<li><a data-i="' + k + '"><span>' + (k + 1) + '</span>' + esc(s.getAttribute('data-title') || '') + '</a></li>'; }).join('');
  menu.addEventListener('click', function (e) { var a = e.target.closest('a[data-i]'); if (a) { show(+a.getAttribute('data-i')); menu.classList.remove('open'); } else if (e.target === menu) menu.classList.remove('open'); });
  document.getElementById('scenes').onclick = function () { menu.classList.toggle('open'); };
  document.addEventListener('keydown', function (e) {
    var t = e.target && e.target.tagName;
    if (t === 'TEXTAREA' || t === 'INPUT') return;
    if (e.key === 'Escape') { menu.classList.remove('open'); return; }
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); show(cur + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(cur - 1); }
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(scenes.length - 1);
    else if (e.key === 'm' || e.key === 'M') menu.classList.toggle('open');
  });
  /* reveal cards */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.rv'); if (!b) return;
    var c = b.closest('.reveal'); c.classList.toggle('open'); b.textContent = c.classList.contains('open') ? 'Hide' : (b.getAttribute('data-label') || 'Show answer');
  });
  /* runnable cells */
  function fmt(o) { return esc(o).replace(/\u0001([\s\S]*?)\u0002/g, '<span class="err">$1</span>'); }
  function norm(s) { return String(s || '').replace(/\u0001|\u0002/g, '').replace(/\s+$/g, '').replace(/^\s+/g, ''); }
  [].forEach.call(document.querySelectorAll('.cell'), function (cell) {
    var ta = cell.querySelector('.code'), out = cell.querySelector('.out'), vars = cell.querySelector('.vars'),
      run = cell.querySelector('.run'), st = cell.querySelector('.st'), expect = cell.getAttribute('data-expect'),
      orig = ta.value, showVars = cell.hasAttribute('data-vars');
    function go() {
      run.disabled = true; st.className = 'st'; st.textContent = PyRun.state() === 'ready' ? 'Running...' : 'Starting Python (first run only, about 10 MB)...';
      out.textContent = '';
      PyRun.run(ta.value, true).then(function (m) {
        run.disabled = false;
        var h = fmt(m.out || '');
        if (m.error) h += '<span class="err">' + esc(m.error) + '</span>';
        if (m.text) h += esc(m.text);
        if (m.html) h += m.html;
        out.innerHTML = h;
        st.textContent = (m.ms / 1000).toFixed(2) + ' s';
        if (showVars) {
          var rows = (m.vars || []);
          vars.innerHTML = rows.length ? '<div class="vt">Variables in memory</div><table><tr><th>name</th><th>type</th><th>value</th></tr>' + rows.map(function (r) { return '<tr><td>' + esc(r[0]) + '</td><td>' + esc(r[1]) + '</td><td>' + esc(r[2]) + '</td></tr>'; }).join('') + '</table>' : '';
        }
        if (expect !== null) {
          var got = norm((m.out || '') + (m.text || ''));
          if (!m.error && got === expect.trim()) { st.className = 'st ok'; st.textContent = 'Correct'; }
          else { st.className = 'st no'; st.textContent = 'Not yet' + (m.error ? ' (error)' : ''); }
        }
      });
    }
    run.onclick = go;
    ta.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); go(); }
      if (e.key === 'Tab') { e.preventDefault(); ta.setRangeText('    ', ta.selectionStart, ta.selectionEnd, 'end'); }
    });
    var cp = cell.querySelector('.copy');
    if (cp) cp.onclick = function () { (window.RMChrome ? RMChrome.copy(ta.value) : Promise.reject()).then(function () { cp.textContent = 'Copied'; setTimeout(function () { cp.textContent = 'Copy'; }, 1400); }, function () {}); };
    var rs = cell.querySelector('.reset');
    if (rs) rs.onclick = function () { ta.value = orig; out.textContent = ''; st.textContent = ''; st.className = 'st'; };
  });
})();
