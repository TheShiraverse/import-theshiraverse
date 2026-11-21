#!/usr/bin/env python3
"""Generates curriculum/CURRICULUM.md and curriculum/curriculum.json from curriculum_data.py."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curriculum_data as c
OUT = HERE.parent / "curriculum"

# validation
nums = [t["n"] for m in c.MODULES for t in m["topics"] if t["n"].isdigit()]
assert [int(x) for x in nums] == list(range(1, 76)), "topic numbers must run 1..75 in order"
for m in c.MODULES:
    for t in m["topics"]:
        assert t["covers"] and t["goal"], t["n"]
        if t["n"].isdigit():
            assert t["traps"] and t["practice"] and t["sql"], f'topic {t["n"]} incomplete'

L = []
L += ["# import TheShiraverse: Python for Data Analysts. Complete curriculum v4",
      "",
      "Generated from `tools/curriculum_data.py` (edit there, then run `python3 tools/build_curriculum_doc.py`). 2026-11-21, DRAFT for Ali's approval.",
      "Site: python.theshiraverse.com. Part of the TheShiraverse Data Science & AI path (SQL, Python, maths, ML, deep learning, NLP/vision, MLOps).",
      "Audited against the official Python tutorial, W3Schools and Kaggle (see AUDIT_2026-11-21.md) and merged with Ali's Aug 2025 Trainer Edition (Sections 1 and 3).",
      "",
      "## Principles",
      "- Beginner-first: orientation, history, `print()` and syntax come before variables. Nothing is assumed.",
      "- Runs in the browser (Pyodide). RetailMart tables first appear in Module 2 (Reading data); Module 1 uses small generic values (Indian retail flavour, ₹).",
      "- Every topic ties back to SQL where a SQL idea exists (the 'SQL bridge' line).",
      "- Real errors on purpose: every topic teaches the mistakes beginners make and the exact error text.",
      "- Self-paced, topic-ordered, no calendar. One topic is about one 2-hour class when taught live.",
      "",
      "## What every topic ships with (the content standard)",
      "Title scene, Agenda, Where we left off, Story, SQL bridge, topic blocks (each: visual + definition/syntax + runnable cells), Common mistakes (broken vs fixed), Pro tip, Real-world cell, Practice Arena (8 questions: Easy, Medium, Hard, Crazy), Interview Studio (5), Self-Check (6), Key Takeaways (6), Quick Reference, Take-Home Challenge, Journey map, Next-topic preview. Built with `tools/build_deck.py`; every cell is verified at build time.",
      ""]
tot_topics = sum(1 for m in c.MODULES for t in m["topics"] if t["n"].isdigit())
L += ["## Map", "", "| Module | Topics | Time |", "|---|---|---|"]
for m in c.MODULES:
    topics = m["topics"]; ds = [t for t in topics if t["n"].isdigit()]
    rng = f'{ds[0]["n"]} to {ds[-1]["n"]}' if ds else f'{topics[0]["n"]} to {topics[-1]["n"]}'
    extra = len(topics) - len(ds) if ds else 0
    L.append(f'| {m["code"]}. {m["title"]} | {len(ds) or len(topics)} ({rng}){" + "+str(extra)+" projects" if extra and m["code"]=="1" else ""} | {m["hours"]} |')
L += ["", f"Total: {tot_topics} numbered topics, 5 Get started sections, 3 mini-projects, 1 capstone. About 164 hours of teaching at 2 h per topic plus projects.", ""]

for m in c.MODULES:
    L += [f'## {"Get started" if m["code"]=="G" else "Module "+m["code"]+": "+m["title"]}', "", f'**Outcome:** {m["outcome"]}', f'**Time:** {m["hours"]}', ""]
    for t in m["topics"]:
        tag = f'{t["n"]}' if not t["n"].isdigit() else f'Topic {t["n"]}'
        L += [f'### {tag}. {t["title"]}' + (" (BUILT)" if t["status"] == "BUILT" else ""), f'**Goal:** {t["goal"]}', "**Covers:**"]
        L += [f"- {x}" for x in t["covers"]]
        if t["sql"]: L.append(f'**SQL bridge:** {t["sql"]}')
        if t["traps"]: L.append("**Common mistakes:** " + "; ".join(t["traps"]))
        L.append("**Practice:** " + "; ".join(t["practice"]))
        L.append("")
L += ["## Not on this site (own courses on the path)", "Maths, classical and advanced ML, deep learning, NLP, computer vision, MLOps. Left out on purpose: Tkinter, Turtle, Django, MySQL/MongoDB drivers.", "",
      "## How content gets prepared (next step)",
      "1. Ali approves this curriculum (or edits `tools/curriculum_data.py`).",
      "2. Per topic, in order: a content file in `tools/topics/` (story, examples, mistakes, 8 practice questions, 5 interview questions) written in Ali's voice; build and verify; Ali reviews on the held page; publish.",
      "3. Get started pages and the notes index are regenerated from this data.",
      "4. Topic numbers are stable from here: change the data file, never renumber by hand.", ""]
(OUT / "CURRICULUM.md").write_text("\n".join(L))
(OUT / "curriculum.json").write_text(json.dumps(c.MODULES, indent=1, ensure_ascii=False))
print("wrote", OUT / "CURRICULUM.md", len("\n".join(L).split()), "words;", tot_topics, "topics")
