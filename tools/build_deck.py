#!/usr/bin/env python3
"""python3 tools/build_deck.py <topic file stem>   e.g. m1_01_variables_data_types"""
import sys, importlib, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "topics"))
import deck_lib
SITE = HERE.parent

def main(stem):
    t = importlib.import_module(stem)
    m = t.META
    scenes = t.build()
    problems = deck_lib.verify_cells()
    if problems:
        print("CELL PROBLEMS:"); [print(" -", p) for p in problems]; sys.exit(1)
    n_practice = sum(1 for c in deck_lib.CELLS if c.get("practice"))
    n_int = sum(s.count('class="reveal"') for s in scenes if "Interview" in s[:200])
    title = m["title"]; url = f'https://python.theshiraverse.com/notes/module-{m["module"]}/{m["slug"]}/'
    chips = [(len(scenes) + 1, "scenes"), (n_practice, "practice questions"), (5, "interview questions"), ("live", "runnable code")]
    ch = "".join(f'<span class="chip"><b>{a}</b> {b}</span>' for a, b in chips)
    first = (f'<section class="scene active" data-title="{title}"><div class="inner"><div class="tag">Module {m["module"]} · Topic {m["num"]}</div>'
             f'<h1><span class="py">import</span> TheShiraverse<br>{title}</h1><p class="lead">{(lambda d: d[0].upper()+d[1:])(m["desc"].split(": ",1)[1])}</p><div class="chips">{ch}</div>'
             f'<div class="mission"><b>Today\'s mission:</b> name a value, know its type, and convert it safely. Press <b>→</b> to move, <b>M</b> for all scenes.</div></div></section>')
    body = first + "\n".join(scenes)
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | import TheShiraverse</title>
<meta name="description" content="{m["desc"]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:site_name" content="TheShiraverse">
<meta property="og:title" content="{title} | import TheShiraverse"><meta property="og:description" content="{m["desc"]}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://python.theshiraverse.com/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/chrome.css"><link rel="stylesheet" href="/assets/deck.css">
<script>window.PYRUN={m["pyrun"]};</script><script src="/assets/pyrun.js"></script>
</head>
<body>
<div class="bar"><a class="brand" href="/notes/">import <b>TheShiraverse</b></a><div class="tools"><a href="/playground/" target="_blank" rel="noopener">Playground</a><button id="scenes" type="button">Scenes (M)</button><button id="prev" type="button" aria-label="Previous scene">&larr;</button><button id="next" type="button" aria-label="Next scene">&rarr;</button></div></div>
<div class="stage">
{body}
</div>
<div class="menu" id="menu"><ol></ol></div>
<div class="progress"></div><div class="foot" id="footinfo"></div>
<script src="/assets/deck.js"></script>
<script src="/assets/chrome.js" defer></script>
</body>
</html>
'''
    out = SITE / "notes" / f'module-{m["module"]}' / m["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    print(f"built {out/'index.html'}  scenes={len(scenes)+1} cells={len(deck_lib.CELLS)} practice={n_practice} bytes={len(page)}")

main(sys.argv[1])
