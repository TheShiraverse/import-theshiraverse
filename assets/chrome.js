/* ============================================================
   Shared site chrome: paints the nav link list and the
   "Get In Touch" footer grid from ONE place into every page.

   Usage, on any page:
     <link rel="stylesheet" href="/assets/chrome.css">
     ...inside the page's own nav container...
       <span id="site-nav-links"></span>
     ...at the bottom, where the footer grid should sit...
       <div id="site-footer-grid"></div>
     ...before </body>...
       <script src="/assets/chrome.js" defer></script>

   #site-nav-links inherits whatever class the surrounding nav
   element already gives its <a> children (each link below is
   rendered with class "l", "l on" when active -- the convention
   already used site-wide). #site-footer-grid gets the full
   "Get In Touch" markup, self-contained, no dependency on the
   host page's own CSS variables.

   Also the site-wide COPY button (so no page needs its own copy code):
     - any element with data-copy="text" copies that text when clicked
       (<button class="yourclass" data-copy="psql ...">Copy</button>);
     - any <pre class="rawcode"> that has no Copy button gets one.
   Uses the Clipboard API and falls back to execCommand('copy') where it
   is unavailable (file://, plain http, old browsers). Pages that still
   carry their own inline copy code keep working: their handlers run
   first and the shared one skips anything already handled.
   Reusable from page scripts as window.RMChrome.copy(text) -> Promise.
   ============================================================ */
(function(){
  var NAV_LINKS = [
    ['/#curriculum', 'Curriculum'],
    ['/notes/', 'Nukte'],
    ['/playground/', 'Playground'],
    ['/practice/', 'Practice'],
    ['https://sql.theshiraverse.com', 'SQL course ↗'],
    ['https://theshiraverse.com/book', 'Book a 1:1'],
    ['https://theshiraverse.com', 'TheShiraverse ↗'],
  ];

  function paintNav(){
    var mount = document.getElementById('site-nav-links');
    if(!mount) return;
    var path = location.pathname;
    var html = NAV_LINKS.map(function(l){
      var href = l[0], label = l[1];
      var isExternal = href.indexOf('http') === 0;
      var isOn = !isExternal && href.indexOf('#') === -1 && href !== '/' && path.indexOf(href) === 0;
      return '<a class="l' + (isOn ? ' on' : '') + '" href="' + href + '"' +
        (isExternal ? ' target="_blank" rel="noopener"' : '') + '>' + label + '</a>';
    }).join('');
    mount.outerHTML = html; // drop the wrapper span, leave plain <a> siblings in the nav
  }

  var ICO = {
    yt: '<svg width="22" height="22" viewBox="0 0 24 24" fill="#ef4444"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
    li: '<svg width="22" height="22" viewBox="0 0 24 24" fill="#3b82f6"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
    wa: '<svg width="22" height="22" viewBox="0 0 24 24" fill="#22c55e"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.821 11.821 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 001.51 5.26l-.999 3.648 3.748-.985z"/></svg>',
    dc: '<svg width="22" height="22" viewBox="0 0 24 24" fill="#a855f7"><path d="M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028 14.09 14.09 0 001.226-1.994.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z"/></svg>',
  };
  function ic(rgba, color, path, stroke){
    var inner = stroke
      ? '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="' + path + '"/></svg>'
      : '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="' + path + '"/></svg>';
    return '<span class="ic" style="background:' + rgba + ';color:' + color + '">' + inner + '</span>';
  }
  var P_WATCH = 'M8 5v14l11-7z';
  var P_BELL = 'M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z';
  var P_SHORTS = 'M13 2L3 14h7v8l10-12h-7V2z';
  var P_LI = 'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z';
  var P_NL = 'M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z';
  var P_WA = 'M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.821 11.821 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 001.51 5.26l-.999 3.648 3.748-.985z';
  var P_DC = 'M20.317 4.37a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 00-5.487 0 12.64 12.64 0 00-.617-1.25.077.077 0 00-.079-.037A19.736 19.736 0 003.677 4.37a.07.07 0 00-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 00.031.057 19.9 19.9 0 005.993 3.03.078.078 0 00.084-.028 14.09 14.09 0 001.226-1.994.076.076 0 00-.041-.106 13.107 13.107 0 01-1.872-.892.077.077 0 01-.008-.128 10.2 10.2 0 00.372-.292.074.074 0 01.077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 01.078.01c.12.098.246.198.373.292a.077.077 0 01-.006.127 12.299 12.299 0 01-1.873.892.077.077 0 00-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 00.084.028 19.839 19.839 0 006.002-3.03.077.077 0 00.032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 00-.031-.03z';

  var FOOTGRID_HTML =
    '<div class="cta-label">Get In Touch</div>' +
    '<p class="uf-tag" style="margin-bottom:20px">Questions, feedback, or just want to say hi &mdash; here\'s where to find us.</p>' +
    '<div class="pgrid">' +
      '<div class="pcard"><div class="pcard-head"><div class="card-icon" style="background:rgba(239,68,68,0.1)">' + ICO.yt + '</div><h3>YouTube</h3></div>' +
      '<p class="pcard-desc">Live sessions &amp; Python tutorials</p>' +
      '<div class="pcard-links" style="margin-top:12px">' +
        '<a href="https://www.youtube.com/@theshiraverse" target="_blank" rel="noopener">' + ic('rgba(239,68,68,.15)', '#ef4444', P_WATCH) + ' Watch</a>' +
        '<a href="https://www.youtube.com/@theshiraverse?sub_confirmation=1" target="_blank" rel="noopener">' + ic('rgba(239,68,68,.15)', '#ef4444', P_BELL) + ' Subscribe</a>' +
        '<a href="https://www.youtube.com/@theshiraverse/shorts" target="_blank" rel="noopener">' + ic('rgba(239,68,68,.15)', '#ef4444', P_SHORTS) + ' Shorts</a>' +
      '</div></div>' +
      '<div class="pcard"><div class="pcard-head"><div class="card-icon" style="background:rgba(59,130,246,0.1)">' + ICO.li + '</div><h3>LinkedIn</h3></div>' +
      '<p class="pcard-desc">Updates, teaching notes &amp; the story behind this channel</p>' +
      '<div class="pcard-links" style="margin-top:12px">' +
        '<a href="https://www.linkedin.com/in/sayyed-shiraj-ali-ahmad" target="_blank" rel="noopener">' + ic('rgba(59,130,246,.15)', '#3b82f6', P_LI) + ' Profile</a>' +
        '<a href="https://www.linkedin.com/newsletters/theshiraverse-7505584123508404225/" target="_blank" rel="noopener">' + ic('rgba(6,182,212,.15)', '#06b6d4', P_NL, true) + ' Newsletter</a>' +
        '<a href="https://www.linkedin.com/company/theshiraverse/" target="_blank" rel="noopener">' + ic('rgba(59,130,246,.15)', '#3b82f6', P_LI) + ' Company</a>' +
      '</div></div>' +
      '<div class="pcard"><div class="pcard-head"><div class="card-icon" style="background:rgba(34,197,94,0.1)">' + ICO.wa + '</div><h3>WhatsApp</h3></div>' +
      '<p class="pcard-desc">Community discussion &amp; video alerts</p>' +
      '<div class="pcard-links" style="margin-top:12px">' +
        '<a href="https://chat.whatsapp.com/JzuixbXtgVs0u9c46GuIc0" target="_blank" rel="noopener">' + ic('rgba(34,197,94,.15)', '#22c55e', P_WA) + ' Community</a>' +
        '<a href="https://whatsapp.com/channel/0029VbCxiGiJf05eJBC59q3R" target="_blank" rel="noopener">' + ic('rgba(34,197,94,.15)', '#22c55e', P_WA) + ' Channel</a>' +
      '</div></div>' +
      '<div class="pcard"><div class="pcard-head"><div class="card-icon" style="background:rgba(168,85,247,0.1)">' + ICO.dc + '</div><h3>Discord</h3></div>' +
      '<p class="pcard-desc">Live-session voice chat &amp; ongoing discussion</p>' +
      '<div class="pcard-links" style="margin-top:12px">' +
        '<a href="https://discord.gg/gABgF8P3pt" target="_blank" rel="noopener">' + ic('rgba(168,85,247,.15)', '#a855f7', P_DC) + ' Join Server</a>' +
      '</div></div>' +
    '</div>';

  function paintFooterGrid(){
    var mount = document.getElementById('site-footer-grid');
    if(!mount) return;
    mount.innerHTML = FOOTGRID_HTML;
  }

  /* ---- shared COPY component (see header) ---- */
  function legacyCopy(text){
    return new Promise(function(resolve, reject){
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-1000px;opacity:0';
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch(e) {}
      document.body.removeChild(ta);
      if(ok) resolve(); else reject(new Error('copy failed'));
    });
  }
  function copyText(text){
    if(navigator.clipboard && window.isSecureContext){
      return navigator.clipboard.writeText(text).catch(function(){ return legacyCopy(text); });
    }
    return legacyCopy(text);
  }
  function flash(btn, label){
    if(!btn.hasAttribute('data-orig')) btn.setAttribute('data-orig', btn.textContent);
    btn.textContent = label;
    clearTimeout(btn._rmT);
    btn._rmT = setTimeout(function(){ btn.textContent = btn.getAttribute('data-orig'); }, 1500);
  }
  function doCopy(btn, text){
    copyText(text).then(function(){ flash(btn, 'Copied'); }, function(){ flash(btn, 'Press Ctrl+C'); });
  }
  document.addEventListener('click', function(e){
    var b = e.target && e.target.closest ? e.target.closest('[data-copy]') : null;
    if(!b) return;
    e.preventDefault();
    doCopy(b, b.getAttribute('data-copy'));
  });
  function addCopyButtons(){
    var pres = document.querySelectorAll('pre.rawcode');
    if(!pres.length) return;
    if(!document.getElementById('rm-copy-css')){
      var st = document.createElement('style'); st.id = 'rm-copy-css';
      st.textContent = '.rm-copy{position:absolute;top:8px;right:8px;background:var(--card,#1a1f2e);border:1px solid var(--border,#2a3040);color:var(--muted,#94a3b8);border-radius:6px;padding:3px 10px;font:500 12px Inter,sans-serif;cursor:pointer}.rm-copy:hover{color:var(--text,#f1f5f9);border-color:var(--accent,#3b82f6)}';
      document.head.appendChild(st);
    }
    [].forEach.call(pres, function(pre){
      if(pre.querySelector('.copybtn,.rm-copy,.wincopy')) return;
      var text = pre.textContent;
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'rm-copy'; b.textContent = 'Copy';
      b.addEventListener('click', function(e){ e.stopPropagation(); doCopy(b, text); });
      pre.style.position = 'relative';
      pre.appendChild(b);
    });
  }
  window.RMChrome = { copy: copyText, addCopyButtons: addCopyButtons };

  // "Watch on YouTube" for the Module 1 class decks, added into each deck's top link row (.rlinks).
  // One place for every deck, so deck files never need editing for this (Ali, 11 Oct 2026).
  var CLASS_VIDEOS = {};
  function paintWatch(){
    var path = location.pathname.replace(/index\.html$/, '');
    if(path.slice(-1) !== '/') path += '/';
    var vids = CLASS_VIDEOS[path];
    var row = document.querySelector('.rlinks');
    if(!vids || !row || row.querySelector('.watch-yt')) return;
    var html = vids.map(function(v){
      return '<a class="watch-yt" href="https://www.youtube.com/watch?v=' + v[1] + '" target="_blank" rel="noopener">&#9654; ' + v[0] + '</a>';
    }).join(' &middot; ');
    row.insertAdjacentHTML('afterbegin', html + ' &middot; ');
  }

  function run(){ paintNav(); paintFooterGrid(); addCopyButtons(); paintWatch(); }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
