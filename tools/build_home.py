#!/usr/bin/env python3
"""Builds index.html from the SQL site's home page (same CSS, nav, ticker, footer) with Python text + curriculum.json."""
import json, re, html, pathlib
SITE = pathlib.Path(__file__).resolve().parent.parent
SQL = pathlib.Path("/Volumes/shira_2/__work__/hussle/TheShiraverse/select-from-shiraverse/index.html").read_text().split("\n")
L = lambda a, b: "\n".join(SQL[a-1:b])          # 1-based inclusive
cur = json.load(open(SITE/"curriculum/curriculum.json"))
e = html.escape

head = L(1, 1076)
head = re.sub(r"<title>.*?</title>", "<title>import TheShiraverse — Python for Data Analysts</title>", head)
desc = "A self-paced Python course for data analysts: from your first print() to pandas, run in your browser. Free to start."
head = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>"+desc, head)
head = re.sub(r'(og:description" content=")[^"]*', r"\g<1>"+desc, head)
head = re.sub(r'(twitter:description" content=")[^"]*', r"\g<1>"+desc, head)
head = head.replace("sql.theshiraverse.com", "python.theshiraverse.com")
head = head.replace("SELECT * FROM TheShiraverse: learn SQL", "import TheShiraverse: learn Python")
head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", head, flags=re.S)
head = head.replace('href="assets/', 'href="/assets/')
mods = [m for m in cur if m["code"] != "G"]
ntop = sum(1 for m in mods for t in m["topics"] if str(t["n"]).isdigit())
hours = sum(int(re.search(r"\d+", m["hours"]).group()) for m in cur)

nav = L(1077, 1093).replace('<span class="sql">SELECT *</span> TheShiraverse', '<span class="sql">import</span> TheShiraverse').replace('src="assets/', 'src="/assets/')
hero = L(1111, 1160)
hero = hero.replace("PostgreSQL 18 &middot; Self-Paced", "Python &middot; pandas &middot; Self-Paced")
hero = hero.replace('Master <span class="gradient">SQL</span> with<br>Real-World Data', 'Master <span class="gradient">Python</span> with<br>Real-World Data')
hero = re.sub(r'<p class="hero-sub">.*?</p>', '<p class="hero-sub">From your first print() to pandas, built around RetailMart — an Indian retail database you already know from the SQL course. Every example runs in your browser. No cohort, no calendar — go at your own speed.</p>', hero, flags=re.S)
stats = [("6","Modules","#curriculum",None), (str(ntop),"Topics","#curriculum",None), (str(hours),"Hours","#curriculum",None), ("10","Tables","/playground/",None)]
sh = "".join(f'<a href="{h}" class="stat-card"><div class="stat-number" data-count="{n}">0</div><div class="stat-label">{l}</div></a>' for n,l,h,_ in stats)
hero = re.sub(r'<div class="hero-stats">.*?</div>\s*(?=<div class="hero-actions">)', '<div class="hero-stats">'+sh+'</div>\n\n        ', hero, flags=re.S)
hero = hero.replace('href="playground/"', 'href="/playground/"').replace("Try SQL Now", "Try Python Now").replace('href="setup/"', 'href="#setup"')
hero = hero.replace("Try SQL in your browser right now, no install. Then set up your own machine and learn at your own pace", "Run Python in your browser right now, no install. Then set up your own machine and learn at your own pace")

icons = {
 "blue":('var(--accent)','<path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>'),
 "purple":('var(--purple)','<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>'),
 "green":('var(--green)','<path d="M5 3l14 9-14 9V3z"/>'),
 "cyan":('var(--cyan)','<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>'),
 "orange":('var(--orange)','<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
 "pink":('var(--pink)','<path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>'),
}
feats = [("blue","Python From Zero","No coding background needed. Start at print() and build up: variables, strings, lists, dicts, loops, functions, files, OOP."),
 ("purple","Real Retail Data","From Module 2 you work on RetailMart as pandas DataFrames — customers, orders, products, stores. Same data as the SQL course."),
 ("green","Run It In Your Browser","Every example is a live cell. Edit, run, break it, fix it. Nothing to install to get started."),
 ("cyan","Practice On Every Topic","Short exercises inside each page, checked as you type, so you know straight away if you got it."),
 ("orange","SQL To Python Bridge","Every topic answers: how did I do this in SQL? Join, group by and window functions become pandas you can read."),
 ("pink","Interview Ready","SQL vs pandas questions, coding rounds and a capstone project, the kind data analyst interviews ask.")]
fcards = "".join(f'''<div class="feature-card"><div class="feature-icon fi-{c}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{icons[c][0]}" stroke-width="2">{icons[c][1]}</svg></div><h3>{e(t)}</h3><p>{e(d)}</p></div>
''' for c,t,d in feats)
features = f'''<div class="container">

    <div class="section reveal" id="features">
        <div class="section-label"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg> Why This Course</div>
        <h2 class="section-title">Built for Real-World Python Skills</h2>
        <p class="section-desc">Not toy examples. You learn Python the way a data analyst uses it, on a realistic business dataset.</p>
        <div class="features-grid">
{fcards}        </div>
    </div>
'''

weeks = ""
for m in mods:
    chips = ""
    for t in m["topics"]:
        chips += f'<li><button class="topic-chip" data-glimpse="{e(", ".join(t["covers"][:6]), quote=True)}">{e(t["title"])}</button></li>\n'
    weeks += f'''<div class="week-card"><div class="week-header"><span class="week-num">MODULE {m["code"]}</span></div><div class="week-title">{e(m["title"])}</div><ul class="week-topics">
{chips}</ul><div class="topic-glimpse"></div></div>
'''
curriculum = f'''    <div class="section reveal" id="curriculum">
        <div class="section-label"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg> Curriculum</div>
        <h2 class="section-title">{ntop} Topics, Interview Prep &amp; Projects, Self-Paced</h2>
        <p class="section-desc">From your first print() to pandas and a capstone. No calendar — work through each module at your own speed. Tap a topic to see what it covers.</p>
        <div class="curriculum-grid">
{weeks}        </div>
    </div>
'''

# Get started cards: reuse the generated links (kept in sync by build_notes_index.py)
gs = [("G1","/notes/get-started/meet-python/","Meet Python","What Python is, where it came from and why analysts use it","purple","M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"),
 ("G2","/notes/get-started/how-python-runs/","How Python runs","Interpreter, scripts, notebooks and your first error","accent","M13 10V3L4 14h7v7l9-11h-7z"),
 ("G3","/notes/get-started/run-in-your-browser/","Run Python in your browser","Use the cells and the playground, no install","green","M5 3l14 9-14 9V3z"),
 ("G4","/notes/get-started/set-up-python/","Set up Python on your laptop","Windows and Mac, VS Code, venv, pip, Jupyter","cyan","M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"),
 ("G5","/notes/get-started/website-walkthrough/","Website walkthrough","Where notes, practice, playground and help live","orange","M4 6h16M4 12h16M4 18h7")]
gcards = "".join(f'''<a class="card" href="{h}"><div class="card-icon" style="background:rgba(59,130,246,0.1)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--{c})" stroke-width="2"><path d="{p}"/></svg></div><div class="card-body"><h3>{e(t)}</h3><p>{e(d)}</p></div></a>
''' for _,h,t,d,c,p in gs)
setup = f'''    <div class="section reveal" id="setup">
        <div class="section-label"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> Get Started <span class="badge badge-free" style="margin-left:0.5rem">Free</span></div>
        <h2 class="section-title">Get Started</h2>
        <p class="section-desc">Five short pages to do once, in order. Then you're ready for Module 1. Videos coming soon.</p>
        <div class="cards-grid">
{gcards}        </div>
    </div>
'''
book = L(1578, 1612).replace("Any doubt in data science, AI, ML, SQL, Python, Excel or Power BI.", "Any doubt in Python, data science, AI, ML, SQL, Excel or Power BI.")
tail = L(1615, len(SQL))
tail = tail.replace("Built by Shiraj Ahmad &middot; PostgreSQL 18 &middot; RetailMart", "Built by Shiraj Ahmad &middot; Python &middot; pandas &middot; RetailMart")
news = '''var NEWS = [
        { href: '/notes/get-started/meet-python/', text: '<b>Get started</b> — five short pages: what Python is, how it runs, set up', c: 'var(--green)' },
        { href: '/playground/', text: '<b>Python Playground</b> — real Python and pandas in your browser, nothing to install', c: 'var(--accent)' },
        { href: '/notes/', text: '<b>Nukte</b> — full written notes for every topic, in plain language', c: 'var(--purple)' },
        { href: 'https://sql.theshiraverse.com', text: '<b>New to data?</b> — learn SQL first on the SQL course', c: 'var(--orange)' }
    ];'''
tail = re.sub(r"var NEWS = \[.*?\n    \];", lambda m: news, tail, flags=re.S)
out = "\n".join([head, nav, hero, features, curriculum, setup, book, "\n</div>\n", tail])
(SITE/"index.html").write_text(out)
print("home built", len(out))
