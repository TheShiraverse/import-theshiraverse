# Python for Data Analysts — curriculum proposal v1 (2026-11-21, DRAFT, awaiting Ali's approval)

Site: python.theshiraverse.com (sister of sql.theshiraverse.com). Runs in the browser with Pyodide (no install needed to start).
Same dataset: RetailMart (CSVs from the SQL course), so every Python topic answers "how did I do this in SQL?".
Same format as the SQL site: topic-ordered, self-paced, Nukte notes decks, practice banks, playground, Get started section.

## Get started (do once)
1. Meet Python (what it is, Python vs SQL vs Excel, what analysts use it for)
2. Run Python in the browser (playground tour) + optional local setup: Python, VS Code, Jupyter
3. Load RetailMart into pandas (same CSVs as SQL)
4. Website walkthrough

## Module 1 — Python Foundations
1 Variables & data types | 2 Numbers & operators | 3 Strings & f-strings | 4 Input, output & errors
5 Lists | 6 Tuples & sets | 7 Dictionaries | 8 Conditions (if/elif/else) | 9 Loops (for/while)
10 Functions | 11 Comprehensions | 12 Files, CSV & JSON | 13 Modules & imports | 14 Error handling

## Module 2 — NumPy & pandas Basics
15 Arrays (NumPy) | 16 Series & DataFrame | 17 Reading data (read_csv) | 18 Selecting columns & rows (loc/iloc)
19 Filtering (the WHERE of pandas) | 20 Sorting, head, unique | 21 New columns & apply | 22 Missing values (NULL handling)
23 Data types & casting | 24 String & date methods

## Module 3 — Analysis with pandas
25 groupby & agg (GROUP BY/HAVING) | 26 Pivot tables & crosstab | 27 merge (all JOIN types)
28 concat & anti-joins | 29 Window-style: rank, cumsum, rolling, shift | 30 Duplicates & data cleaning
31 Dates & time series (resample) | 32 Subtotals & percent-of-total

## Module 4 — Visualisation & Storytelling
33 matplotlib basics | 34 Chart choice for analysts | 35 seaborn | 36 Dashboard-style summaries | 37 Reporting to Excel

## Module 5 — Analyst Toolkit
38 SQL from Python (sqlite/Postgres) | 39 Cohort & RFM in pandas | 40 Funnels | 41 A/B testing basics (scipy)
42 Automating a report | 43 APIs & web data | 44 Git for analysts

## Module 6 — Interview Prep & Capstone
45 Python interview patterns | 46 pandas interview patterns | 47 SQL vs pandas side by side | Capstone: RetailMart analysis end to end

## Open decisions for Ali
- Cut/keep: 44 topics + capstone (SQL has 60); too long for v1? Suggest launching Modules 1-3 first.
- Scikit-learn / ML: out of v1 (suggest a later Module 7).
- Order of build: scaffold site (clone SQL chrome/templates/playground with Pyodide) -> Get started -> Module 1.
- Repo: new GitHub repo TheShiraverse/python-theshiraverse + Cloudflare project (same as SQL). Local folder: needs your OK (STRUCTURE.md forbids new top-level; proposal: releases/python-theshiraverse/).
