# import TheShiraverse: Python for Data Analysts, curriculum v3 (2026-11-21, DRAFT, audited against public references: see AUDIT_2026-11-21.md)

Site: python.theshiraverse.com. Part of the TheShiraverse Data Science & AI path (SQL -> Python -> maths -> ML -> deep learning -> NLP/vision -> MLOps).
Runs in the browser (Pyodide). Dataset: RetailMart. Every topic links back to SQL ("how did I do this in SQL?").
Numbering changed in v3: the built deck "Variables & Data Types" is now topic 2 (topic 1 is Hello Python).

## Get started (do once, 6 short sections)
G1 Meet Python: what it is, a short history (Guido, 1991, why the name), Python 2 vs 3, who uses it, why analysts choose it, Python vs SQL vs Excel
G2 How Python runs: interpreter, REPL, scripts (.py), notebooks (.ipynb), what happens when you press Run
G3 Run Python in your browser (playground tour)
G4 Set up Python on your laptop: install (python.org / Anaconda), VS Code, Jupyter, virtual environments (venv/conda), pip
G5 Load RetailMart into pandas
G6 Website walkthrough

## Module 1: Python Foundations (29 topics + 3 mini-projects)
1 Hello Python: print() (sep, end, many arguments), comments, syntax and indentation, statements and line continuation, help(), PEP 8 and the Zen of Python
2 Variables & data types (BUILT): names, assignment, multiple assignment, int/float/str/bool/None, type(), casting, constants, del
3 Numbers & operators: arithmetic, // % **, precedence, round/divmod/abs, math module, floats vs Decimal vs Fraction, complex, bitwise note
4 Strings 1: indexing, slicing, immutability, escape characters, raw strings, triple quotes, len, in
5 Strings 2: methods (split/join/strip/replace/find), f-strings, format(), % formatting
6 Booleans, comparison & logic: ==, !=, <, and/or/not, is vs ==, in, truthiness, None, short-circuit
7 Input & output: input(), converting input, formatted output, printing tables
8 Conditions: if/elif/else, nested, ternary, match statement
9 Lists 1: create, index, slice, add/remove, methods, sort with key
10 Lists 2: references vs copies (shallow/deep), nested lists, stacks and queues, del, unpacking
11 Tuples & sets: immutability, packing/unpacking, set operations, frozenset
12 Dictionaries: key/value, methods, nested, iterating, Counter and defaultdict
13 Loops 1: for, range(), enumerate, zip, looping over dicts, looping techniques
14 Loops 2: while, break/continue, loop else, pass, nested loops
15 Comprehensions: list, set, dict, generator expressions
16 Functions 1: def, parameters, return, scope (local/global), docstrings
17 Functions 2: default and keyword arguments (the mutable-default trap), *args/**kwargs, unpacking arguments, type hints
18 Functions 3: lambda, map/filter/sorted/any/all, recursion, closures, decorators (intro)
19 Iterators & generators: iter/next, yield, lazy evaluation, why it matters for big files
20 Modules, packages & the standard library: import styles, `__name__ == "__main__"`, pip, math/random/statistics/collections/itertools
21 Dates & times: datetime, timedelta, formatting and parsing, time zones
22 Text patterns: regular expressions with re
23 Files: reading and writing text, with, pathlib and os
24 CSV & JSON: csv module, json module, nested data
25 Errors & debugging: reading tracebacks, try/except/else/finally, raise, custom exceptions, assert, logging, pdb
26 Classes & objects (OOP 1): class, __init__, self, instance vs class variables, methods
27 Inheritance & friends (OOP 2): inheritance, super(), polymorphism, encapsulation, dunder methods, @property, @classmethod, @staticmethod
28 Dataclasses, clean code & simple tests: dataclasses, naming, PEP 8 in practice, assert, doctest, pytest basics
29 Git & GitHub basics for analysts: repo, commit, branch, push, a portfolio repo
Mini-projects: Student grade calculator (CSV in, CSV out) | Expense tracker CLI (CSV/JSON store) | Basic data analysis tool (load CSV, describe, plot)

## Module 2: NumPy & pandas Basics (14)
30 NumPy arrays | 31 Indexing, slicing & boolean masks | 32 Maths, broadcasting & statistics | 33 Random numbers & reproducibility (seeds)
34 Series | 35 DataFrame | 36 Reading and writing data (csv, excel, json, sql, parquet) | 37 Selecting: loc, iloc, index
38 Filtering: the WHERE of pandas, query() | 39 Sorting, head, unique, value_counts | 40 New columns: assign, apply, map, vectorised
41 Missing values (NULL handling) | 42 Data types & casting (category) | 43 String and date accessors (.str, .dt)

## Module 3: Analysis with pandas (12)
44 groupby, agg, named aggregation, transform | 45 Pivot tables & crosstab | 46 Reshaping: melt, stack, unstack | 47 merge: all JOIN types
48 concat & anti-joins | 49 rank, cumsum, rolling, expanding, shift, diff (window functions) | 50 Duplicates & data cleaning
51 Outliers & binning (cut, qcut) | 52 Time series: resample | 53 Subtotals & percent-of-total | 54 describe, quantiles & correlation
55 Performance: vectorise vs loops, chunked reading, memory, timeit

## Module 4: Visualisation & Storytelling (7)
56 matplotlib basics | 57 Customising: labels, subplots, saving | 58 Choosing the right chart | 59 seaborn | 60 plotly (interactive)
61 Dashboard-style summaries | 62 Reporting to Excel and telling the story

## Module 5: Analyst Toolkit (9)
63 Data preprocessing: scaling, encoding (the bridge to the ML course) | 64 SQL from Python (sqlite3, SQLAlchemy, Postgres) | 65 Cohort & RFM
66 Funnels | 67 A/B testing basics (scipy) | 68 Automating a report (scripts, argparse, scheduling) | 69 APIs with requests
70 Web scraping basics | 71 Jupyter best practices & project structure

## Module 6: Interview Prep & Capstone
72 Core Python interview patterns (strings, lists, dicts, two pointers, complexity) | 73 pandas interview patterns | 74 SQL vs pandas side by side
75 Algorithms basics (searching, sorting, Big-O) | Capstone: RetailMart analysis end to end

## Not on this site (other courses of the path)
Maths, classical and advanced ML, deep learning, NLP, computer vision, MLOps. Also left out: Tkinter, Turtle, Django, database drivers for MySQL/MongoDB.
