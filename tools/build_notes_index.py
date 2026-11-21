#!/usr/bin/env python3
"""Regenerates notes/index.html and the Get started steps on the home page from curriculum_data.py + which decks exist."""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curriculum_data as c
SITE = HERE.parent
# deck locations that exist on disk (slug paths registered here)
LIVE = {"G1": "/notes/get-started/meet-python/", "G2": "/notes/get-started/how-python-runs/", "G3": "/notes/get-started/run-in-your-browser/",
        "G4": "/notes/get-started/set-up-python/", "G5": "/notes/get-started/website-walkthrough/", "2": "/notes/module-1/variables-data-types/"}
for k, v in LIVE.items():
    assert (SITE / v.strip("/") / "index.html").exists(), f"missing deck for {k}: {v}"

def row(t):
    href = LIVE.get(t["n"])
    num = t["n"] if not t["n"].isdigit() else f'{int(t["n"]):02d}'
    return ('<a class="nt live" href="%s"><span class="n mono">%s</span><b>%s</b><span class="s">Open the deck</span></a>' % (href, num, t["title"]) if href else
            '<a class="nt soon"><span class="n mono">%s</span><b>%s</b><span class="s">Coming soon</span></a>' % (num, t["title"]))

idx = (SITE / "notes" / "index.html").read_text()
head = idx[:idx.index('<div class="wrap"')]
foot = idx[idx.index('<div id="site-footer-grid"'):]
body = ['<div class="wrap" style="padding-top:56px"><div class="mono" style="color:var(--accent-l);font-size:.8rem;letter-spacing:2px">NUKTE</div>'
        '<h1 style="font-size:2.2rem;margin:6px 0">Python notes, one deck per topic</h1>'
        '<p class="sub">Each deck is a full-screen runnable lesson: story, syntax, mistakes, practice, interview questions. Press &rarr; to move, M for all scenes. Decks are published as they are finished.</p>']
for m in c.MODULES[:2]:
    title = "Get started" if m["code"] == "G" else f'Module {m["code"]}: {m["title"]}'
    body.append(f'<h2>{title}</h2><div class="nl">' + "".join(row(t) for t in m["topics"]) + "</div>")
body.append('<h2>Modules 2 to 6</h2><p class="sub">NumPy &amp; pandas, Analysis, Visualisation, the Analyst Toolkit, and Interview Prep come after Module 1. See the <a href="/#curriculum">curriculum</a>.</p></div>\n')
(SITE / "notes" / "index.html").write_text(head + "".join(body) + foot)

# home page: Get started steps link to the real pages
h = (SITE / "index.html").read_text()
steps = "".join(f'<a href="{LIVE[t["n"]]}" style="text-decoration:none;color:inherit"><div><b>{i+1}</b>{lab}</div></a>' for i, (t, lab) in enumerate(zip(c.MODULES[0]["topics"], [
    "Meet Python: what it is and where it came from", "How Python runs: interpreter, scripts, notebooks", "Run Python in your browser",
    "Set up Python on your laptop", "Website walkthrough"])))
new = f'<div class="steps">{steps}</div>'
h2 = re.sub(r'<div class="steps">.*?</div></div>(?=\s*<h2 id="curriculum")', new, h, flags=re.S)
assert h2 != h or new in h, "home steps block not replaced"
(SITE / "index.html").write_text(h2)
# sitemap: home, playground, notes index and every live deck
urls = ["/", "/playground/", "/notes/"] + list(LIVE.values())
(SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>https://python.theshiraverse.com{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("notes index + home + sitemap updated")
