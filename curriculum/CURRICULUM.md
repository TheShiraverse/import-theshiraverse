# import TheShiraverse: Python for Data Analysts. Complete curriculum v4

Generated from `tools/curriculum_data.py` (edit there, then run `python3 tools/build_curriculum_doc.py`). 2026-11-21, DRAFT for Ali's approval.
Site: python.theshiraverse.com. Part of the TheShiraverse Data Science & AI path (SQL, Python, maths, ML, deep learning, NLP/vision, MLOps).
Audited against the official Python tutorial, W3Schools and Kaggle (see AUDIT_2026-11-21.md) and merged with Ali's Aug 2025 Trainer Edition (Sections 1 and 3).

## Principles
- Beginner-first: orientation, history, `print()` and syntax come before variables. Nothing is assumed.
- Runs in the browser (Pyodide). RetailMart tables first appear in Module 2 (Reading data); Module 1 uses small generic values (Indian retail flavour, ₹).
- Every topic ties back to SQL where a SQL idea exists (the 'SQL bridge' line).
- Real errors on purpose: every topic teaches the mistakes beginners make and the exact error text.
- Self-paced, topic-ordered, no calendar. One topic is about one 2-hour class when taught live.

## What every topic ships with (the content standard)
Title scene, Agenda, Where we left off, Story, SQL bridge, topic blocks (each: visual + definition/syntax + runnable cells), Common mistakes (broken vs fixed), Pro tip, Real-world cell, Practice Arena (8 questions: Easy, Medium, Hard, Crazy), Interview Studio (5), Self-Check (6), Key Takeaways (6), Quick Reference, Take-Home Challenge, Journey map, Next-topic preview. Built with `tools/build_deck.py`; every cell is verified at build time.

## Map

| Module | Topics | Time |
|---|---|---|
| G. Get started | 5 (G1 to G5) | about 4 h |
| 1. Python Foundations | 29 (1 to 29) + 3 projects | about 60 h |
| 2. NumPy & pandas Basics | 14 (30 to 43) | about 28 h |
| 3. Analysis with pandas | 12 (44 to 55) | about 24 h |
| 4. Visualisation & Storytelling | 7 (56 to 62) | about 14 h |
| 5. Analyst Toolkit | 9 (63 to 71) | about 18 h |
| 6. Interview Prep & Capstone | 4 (72 to 75) | about 16 h |

Total: 75 numbered topics, 5 Get started sections, 3 mini-projects, 1 capstone. About 164 hours of teaching at 2 h per topic plus projects.

## Get started

**Outcome:** Know what Python is, how it runs, and have a place to run code (browser or laptop).
**Time:** about 4 h

### G1. Meet Python
**Goal:** Explain what Python is, where it came from and why analysts use it.
**Covers:**
- What Python is and what it is used for
- a short history (Guido van Rossum, first release 1991, the name)
- Python 2 vs Python 3
- who uses Python (data, web, automation, AI)
- Python vs SQL vs Excel for an analyst
- what this course will and will not cover
**SQL bridge:** SQL asks a database a question; Python is a general language that can also ask the database, clean the answer, chart it and automate it
**Common mistakes:** Installing Python 2 by mistake; thinking Python replaces SQL; expecting to learn everything in one week
**Practice:** Match 6 jobs to the right tool (SQL, Excel, Python); a 3-line 'my goal with Python' note

### G2. How Python runs
**Goal:** Describe what happens between writing code and seeing output.
**Covers:**
- Interpreter and bytecode in one picture
- REPL (interactive prompt) vs script (.py) vs notebook (.ipynb)
- running a script from a terminal
- what a Python version is
- errors vs output
- the role of files and folders
**SQL bridge:** SQL runs inside a database server; Python runs in an interpreter on your machine (or here in the browser)
**Common mistakes:** Saving a file as .py.txt; running in the wrong folder; confusing the REPL prompt with code
**Practice:** Run the same 3 lines in REPL, as a script, and in a notebook and compare

### G3. Run Python in your browser
**Goal:** Use the playground to run, edit and re-run code with no install.
**Covers:**
- Tour of the playground
- running a cell
- reading output and errors
- what runs in the browser (pure Python, pandas, NumPy) and what does not
- keyboard shortcuts
**SQL bridge:** Like the SQL playground, but for Python
**Common mistakes:** Expecting files to persist; closing the tab and losing work (copy your code)
**Practice:** Run and change 5 example cells

### G4. Set up Python on your laptop
**Goal:** Have Python, VS Code and Jupyter working, in a clean environment.
**Covers:**
- Installing Python (python.org) or Anaconda/Miniconda
- VS Code and the Python extension
- Jupyter Notebook/JupyterLab
- virtual environments with venv and conda
- pip install/uninstall/list
- requirements.txt
- Windows and Mac differences
**SQL bridge:** Same idea as installing PostgreSQL and pgAdmin in the SQL course
**Common mistakes:** Not activating the environment; installing packages globally; two Pythons on PATH
**Practice:** Create an env called ds_env, install pandas, print its version

### G5. Website walkthrough
**Goal:** Know where notes, practice, playground and help live.
**Covers:**
- Nukte notes
- the Practice banks
- the playground
- how topics are ordered
- how to ask for help and book a 1:1
**SQL bridge:** Same layout as the SQL site
**Common mistakes:** Skipping the practice arena
**Practice:** Find one topic, its practice set and the playground

## Module 1: Python Foundations

**Outcome:** Write, read and debug everyday Python: values, text, collections, control flow, functions, files, errors and small classes.
**Time:** about 60 h

### Topic 1. Hello Python
**Goal:** Write and run first programs and read simple code.
**Covers:**
- print() with several arguments, sep and end
- text in quotes
- comments (#)
- statements and line continuation
- indentation defines blocks
- syntax errors
- help() and dir()
- PEP 8 and the Zen of Python (import this)
**SQL bridge:** SELECT shows a result; print() shows output. SQL ends with ;, Python ends with a new line
**Common mistakes:** Missing quotes or brackets; mixing tabs and spaces (IndentationError); print without brackets (Python 2 habit)
**Practice:** Print a receipt header; fix 5 broken one-liners

### Topic 2. Variables & data types (BUILT)
**Goal:** Name values, know their types and convert between them safely.
**Covers:**
- Assignment
- naming rules and snake_case
- multiple assignment
- int, float, str, bool, None
- type()
- casting with int()/float()/str()/bool()
- constants by convention
- del
- swapping
**SQL bridge:** Python types vs SQL column types (INT, NUMERIC, TEXT, BOOLEAN, NULL)
**Common mistakes:** NameError; str + int TypeError; float drift 0.1+0.2; bool('False') is True
**Practice:** 8 practice questions (built); take-home on a second product

### Topic 3. Numbers & operators
**Goal:** Do arithmetic correctly, including rounding and exact money.
**Covers:**
- + - * / // % **
- operator precedence and brackets
- augmented assignment (+=)
- abs, round, divmod, min, max
- math module
- float vs Decimal vs Fraction
- complex numbers (brief)
- bitwise operators (note)
- underscores in literals
**SQL bridge:** PostgreSQL integer division, POWER, MOD, ROUND, GREATEST/LEAST
**Common mistakes:** ZeroDivisionError; round(2.5) is 2; -7 // 2 is -4; ^ is XOR not power; Decimal + float TypeError
**Practice:** GST invoice; splitting an amount; change-making

### Topic 4. Strings 1: text basics
**Goal:** Slice and inspect text confidently.
**Covers:**
- Quotes, escapes and raw strings
- triple-quoted text
- concatenation and repetition
- len
- indexing and negative indexing
- slicing [start:stop:step]
- immutability
- in and comparison
**SQL bridge:** SUBSTRING, LENGTH, || and LIKE
**Common mistakes:** IndexError; TypeError on item assignment; off-by-one slices; backslashes in Windows paths
**Practice:** Mask a card number; extract an area code; reverse with a slice

### Topic 5. Strings 2: methods & formatting
**Goal:** Clean and format text.
**Covers:**
- upper/lower/title
- strip
- split/join
- replace
- find/index/count
- startswith/endswith
- isdigit/isalpha
- f-strings (width, precision, thousands)
- format()
- % formatting
**SQL bridge:** UPPER, TRIM, SPLIT_PART, REPLACE, TO_CHAR
**Common mistakes:** Methods return new strings; split(' ') vs split(); quotes inside f-strings
**Practice:** Clean names; format invoice lines; parse 'name,city'

### Topic 6. Booleans, comparison & logic
**Goal:** Write correct conditions.
**Covers:**
- True/False
- comparison operators and chaining
- and/or/not and precedence
- short-circuit
- is vs ==
- in / not in
- truthiness (0, '', None, empty collections)
- None
- bool()
**SQL bridge:** WHERE logic, IS NULL, IN; how Python None differs from SQL NULL
**Common mistakes:** x == None; if x == 1 or 2; comparing floats; bool('False')
**Practice:** Eligibility rules; truthiness quiz; input validation

### Topic 7. Input & output
**Goal:** Take input, validate it and print neat output.
**Covers:**
- input() always returns str
- converting and validating
- formatted output and alignment
- printing small tables
- end/sep
- stdout vs stderr
- browser note (simulated input)
**SQL bridge:** SQL has parameters, not input()
**Common mistakes:** int(input()) ValueError; forgetting to convert; unclear prompts
**Practice:** Bill splitter; tip calculator; a tiny form

### Topic 8. Conditions
**Goal:** Make programs choose.
**Covers:**
- if/elif/else
- nested conditions
- conditional expression (ternary)
- match/case (literals, or-patterns, guards)
- pass as placeholder
- indentation
**SQL bridge:** CASE WHEN
**Common mistakes:** = vs ==; elif order; match with no default; deep nesting
**Practice:** Discount tiers; grade bands; order-status router

### Topic 9. Lists 1
**Goal:** Store and process ordered collections.
**Covers:**
- Create
- index and negative index
- slicing
- append/extend/insert
- remove/pop/del
- len/min/max/sum
- sort() vs sorted()
- key=
- reverse
- in, count, index
**SQL bridge:** ORDER BY, LIMIT; arrays
**Common mistakes:** sort() returns None; IndexError; changing a list while looping
**Practice:** Top-3 prices; median; sort orders by total

### Topic 10. Lists 2: references & copies
**Goal:** Avoid the silent bugs of shared lists.
**Covers:**
- Aliasing vs copying
- shallow vs deep copy
- nested lists and grids
- stacks and queues (append/pop, deque)
- del and slice assignment
- unpacking and *rest
**SQL bridge:** Rows are copies; Python lists are shared references
**Common mistakes:** b = a changes a; [[0]*3]*3; mutating a default argument (preview)
**Practice:** Matrix transpose; undo stack; rotate a list

### Topic 11. Tuples & sets
**Goal:** Use fixed records and unique collections.
**Covers:**
- Tuple literals and immutability
- packing/unpacking
- returning several values
- namedtuple (brief)
- sets: uniqueness, union, intersection, difference, symmetric difference
- frozenset
- speed of membership
- set vs list
**SQL bridge:** UNION, INTERSECT, EXCEPT, DISTINCT
**Common mistakes:** (5) is not a tuple, (5,) is; sets are unordered; unhashable items; {} is a dict
**Practice:** Customers in both campaigns; unique cities; swap with tuples

### Topic 12. Dictionaries
**Goal:** Model records and lookups.
**Covers:**
- Key/value pairs
- get(), setdefault()
- keys/values/items
- add/update/pop/del
- nested dicts
- iterating
- merging with | and update()
- Counter and defaultdict
- dict as lookup table
- JSON-like records
**SQL bridge:** GROUP BY counts; lookup joins
**Common mistakes:** KeyError; unhashable keys; changing a dict while iterating
**Practice:** Count order statuses; price lookup; group orders by city

### Topic 13. Loops 1: for
**Goal:** Repeat work over collections.
**Covers:**
- for over lists, strings, dicts
- range(start, stop, step)
- enumerate
- zip
- reversed and sorted
- accumulator patterns (sum, count, max)
- nested loops intro
**SQL bridge:** Set-based SQL vs row-by-row loops: why pandas replaces most loops
**Common mistakes:** Off-by-one in range; changing a list while looping; reusing the loop variable
**Practice:** Total of order amounts; FizzBuzz; multiplication table

### Topic 14. Loops 2: while & control
**Goal:** Repeat until a condition and control the flow.
**Covers:**
- while and sentinels
- infinite loops
- break
- continue
- loop else
- pass
- nested loops
- retry patterns
**SQL bridge:** Recursive CTE idea
**Common mistakes:** Infinite loop; forgetting to update the condition; misreading loop else
**Practice:** Retry a payment 3 times; first prime; simulated guessing game

### Topic 15. Comprehensions
**Goal:** Build collections in one readable line.
**Covers:**
- List, set and dict comprehensions
- conditions
- nested comprehensions
- vs map/filter
- generator expressions
- when not to use them
**SQL bridge:** SELECT expression ... WHERE ...
**Common mistakes:** Over-complex one-liners; side effects inside; variable leakage
**Practice:** Convert prices; filter premium products; invert a dict

### Topic 16. Functions 1
**Goal:** Package logic into reusable functions.
**Covers:**
- def and calling
- parameters vs arguments
- return vs print
- multiple return values
- None
- local vs global scope
- docstrings
- helper functions
**SQL bridge:** User-defined functions in PostgreSQL
**Common mistakes:** Forgetting return; changing globals; UnboundLocalError
**Practice:** gst(); is_valid_phone(); summarise(order)

### Topic 17. Functions 2: arguments
**Goal:** Design flexible function signatures.
**Covers:**
- Default and keyword arguments
- the mutable-default trap
- positional-only and keyword-only
- *args and **kwargs
- unpacking with * and **
- type hints and annotations
- pure functions
**SQL bridge:** Function parameters with DEFAULT
**Common mistakes:** Default list shared between calls; wrong argument order; **kwargs typos
**Practice:** Flexible report(); discount(price, pct=10); a wrapper

### Topic 18. Functions 3: functional tools
**Goal:** Use functions as values.
**Covers:**
- lambda
- key= with lambda
- map, filter, sorted, min, max, any, all, sum
- recursion (base case, factorial, Fibonacci)
- closures
- decorators (a timing decorator)
**SQL bridge:** ORDER BY expressions; aggregate functions
**Common mistakes:** Recursion depth; lambda overuse; late-binding closures
**Practice:** Sort orders by total; recursive sum; timing decorator

### Topic 19. Iterators & generators
**Goal:** Process data lazily.
**Covers:**
- Iterable vs iterator
- iter/next
- StopIteration
- yield and generator functions
- generator expressions
- memory benefits
- itertools (islice, chain)
**SQL bridge:** Cursors and streaming results
**Common mistakes:** Exhausted generators; converting to list too early
**Practice:** Read a big file lazily; batch iterator; running totals

### Topic 20. Modules, packages & the standard library
**Goal:** Reuse code and install libraries.
**Covers:**
- import styles
- writing a module
- packages
- __name__ == '__main__'
- module search path
- dir()
- pip and requirements.txt
- tour: math, random (seed), statistics, collections, itertools, timeit
**SQL bridge:** Schemas and extensions
**Common mistakes:** Naming a file random.py; circular imports; installing into the wrong environment
**Practice:** Dice simulation with a seed; statistics of prices; a tiny utility module

### Topic 21. Dates & times
**Goal:** Work with dates without the usual bugs.
**Covers:**
- date, time, datetime, timedelta
- strftime/strptime and format codes
- ISO format
- comparing and subtracting
- weekday, month ends
- time zones with zoneinfo (IST)
- epoch
**SQL bridge:** DATE_TRUNC, EXTRACT, intervals
**Common mistakes:** Naive vs aware datetimes; %m vs %M; DD/MM vs MM/DD; month arithmetic
**Practice:** Age; days between orders; last day of month; parse mixed date strings

### Topic 22. Text patterns: regex
**Goal:** Find and extract patterns in text.
**Covers:**
- re.search/match/findall/sub/split
- character classes
- quantifiers
- anchors
- groups and named groups
- greedy vs lazy
- flags
- compile
- validating phone/email shapes
**SQL bridge:** LIKE, SIMILAR TO and ~ in PostgreSQL
**Common mistakes:** match vs search; forgetting to escape; greedy surprises
**Practice:** Extract phone numbers; mask digits; parse log lines

### Topic 23. Files
**Goal:** Read and write text files safely.
**Covers:**
- open modes (r, w, a)
- with
- read/readline/readlines
- looping over lines
- write and append
- encoding (utf-8)
- pathlib.Path (exists, glob, mkdir, read_text)
- os basics
- relative vs absolute paths
**SQL bridge:** COPY
**Common mistakes:** Forgetting with/close; encoding errors; overwriting with 'w'; Windows paths
**Practice:** Word count; log filter; write a report file

### Topic 24. CSV & JSON
**Goal:** Read and write the two most common data formats.
**Covers:**
- csv.reader/DictReader/writer
- delimiters, quoting, headers
- everything is str
- json.load/dump/loads/dumps
- nested JSON
- flattening
- pretty printing
- dates in JSON
**SQL bridge:** COPY ... CSV; JSONB
**Common mistakes:** Numbers are strings in CSV; missing newline=''; tuples and datetimes are not JSON
**Practice:** Sum a CSV column; CSV to JSON; flatten nested orders

### Topic 25. Errors & debugging
**Goal:** Read errors, handle them and find bugs.
**Covers:**
- Syntax errors vs exceptions
- reading a traceback
- common exceptions (NameError, TypeError, ValueError, KeyError, IndexError, ZeroDivisionError, FileNotFoundError)
- try/except/else/finally
- raise
- custom exceptions
- chaining
- assert
- logging levels
- print debugging
- pdb
- EAFP vs LBYL
**SQL bridge:** Constraint errors and SQLSTATE
**Common mistakes:** Bare except; swallowing errors; catching too much
**Practice:** safe_int(); retrying reader; validate a record with a custom exception

### Topic 26. Classes & objects (OOP 1)
**Goal:** Model real things as objects.
**Covers:**
- class and object
- __init__ and self
- attributes and methods
- instance vs class variables
- __str__ and __repr__
- objects are references
- when to use a class
**SQL bridge:** A table row is like an object
**Common mistakes:** Forgetting self; mutable class variable; str vs repr
**Practice:** Customer class; BankAccount; Cart

### Topic 27. Inheritance & friends (OOP 2)
**Goal:** Extend and reuse classes.
**Covers:**
- Inheritance and super()
- overriding
- polymorphism and duck typing
- encapsulation (_ and __)
- @property
- @classmethod
- @staticmethod
- dunder methods (__len__, __eq__, __lt__, __add__, __contains__)
- composition vs inheritance
**SQL bridge:** Views and inheritance of tables (INHERITS)
**Common mistakes:** Overriding without super(); multiple-inheritance confusion; name mangling
**Practice:** Shape hierarchy; comparable products; Order with a total property

### Topic 28. Dataclasses, clean code & tests
**Goal:** Write code others can read and trust.
**Covers:**
- dataclass (defaults, frozen, order)
- PEP 8 in practice
- naming
- short functions
- docstrings
- type hints
- assert and doctest
- pytest basics
- a code-review checklist
**SQL bridge:** Naming conventions and migrations
**Common mistakes:** Mutable default in a dataclass (use default_factory); tests that test nothing
**Practice:** Refactor a messy script; write 5 tests

### Topic 29. Git & GitHub basics
**Goal:** Version your work and publish a portfolio.
**Covers:**
- Repo, init/clone
- add/commit
- status/log/diff
- branches and merge
- push/pull
- .gitignore
- README
- a GitHub profile
- good commit messages
**SQL bridge:** The same repo habits as the SQL course
**Common mistakes:** Committing data or secrets; huge files; force-push
**Practice:** Create a portfolio repo with the mini-project

### P1. Mini-project: Student grade calculator
**Goal:** Combine files, loops, dicts and functions.
**Covers:**
- Read a CSV of marks
- total, average and grade by thresholds
- write results to a new CSV
- handle bad rows
**Practice:** Deliver script + output CSV + README

### P2. Mini-project: Expense tracker CLI
**Goal:** Build a small command-line tool.
**Covers:**
- Add expenses (date, category, amount)
- store in CSV/JSON
- totals by category and date range
- menu loop
- validation
**Practice:** Deliver script + sample data + README

### P3. Mini-project: Basic data analysis tool
**Goal:** Prepare for pandas by doing it by hand.
**Covers:**
- Load a CSV
- show first rows
- compute mean, median, mode, std by hand
- text histogram or matplotlib bar chart
**Practice:** Deliver script + chart + README

## Module 2: NumPy & pandas Basics

**Outcome:** Load, inspect, select, filter and clean tables with pandas.
**Time:** about 28 h

### Topic 30. NumPy arrays
**Goal:** Use arrays instead of lists for numbers.
**Covers:**
- Why NumPy (speed)
- ndarray
- dtype
- shape, ndim, size
- array, zeros, ones, arange, linspace
- reshape
- list vs array
**SQL bridge:** A column as a vector
**Common mistakes:** dtype upcasting; shape mismatch
**Practice:** Price array; discounted prices; reshape

### Topic 31. Indexing, slicing & boolean masks
**Goal:** Select parts of arrays.
**Covers:**
- 1D/2D indexing and slicing
- views vs copies
- boolean masks
- fancy indexing
- np.where
- sort and argsort
**SQL bridge:** WHERE
**Common mistakes:** Modifying a view changes the original; & vs and; missing brackets around conditions
**Practice:** Orders above ₹50,000; replace values with where

### Topic 32. Maths, broadcasting & statistics
**Goal:** Compute on whole arrays at once.
**Covers:**
- Vectorised operations
- broadcasting rules
- sum/mean/median/std/var/min/max/percentile
- axis
- cumsum
- NaN-aware functions
- correlation
**SQL bridge:** AVG, STDDEV, PERCENTILE_CONT
**Common mistakes:** Axis confusion; NaN propagates; integer overflow
**Practice:** Z-scores; column means; cumulative revenue

### Topic 33. Random numbers & reproducibility
**Goal:** Simulate and sample reproducibly.
**Covers:**
- default_rng and seeds
- integers, random, choice, normal
- shuffle and sample
- simple simulations (coin, dice)
- bootstrap idea
**SQL bridge:** RANDOM(), TABLESAMPLE
**Common mistakes:** Global seed vs generator; same seed, different order of calls
**Practice:** Simulate delivery times; sample customers

### Topic 34. Series
**Goal:** Work with one labelled column.
**Covers:**
- Create from list/dict/array
- index and labels vs positions
- vectorised operations
- alignment
- name and dtype
- head, sum, value_counts
**SQL bridge:** A single column
**Common mistakes:** Index alignment surprises; label vs position
**Practice:** Price series operations

### Topic 35. DataFrame
**Goal:** Work with a table.
**Covers:**
- Create from dict, list of dicts, NumPy
- columns, index, shape
- info, describe, head, tail
- dtypes
- select one vs several columns
- rename, drop
- set_index/reset_index
- copy
**SQL bridge:** A table
**Common mistakes:** SettingWithCopyWarning; confusing index with a column
**Practice:** Build a small orders DataFrame

### Topic 36. Reading & writing data
**Goal:** Load real data into pandas and save results.
**Covers:**
- read_csv (sep, usecols, dtype, parse_dates, nrows, na_values)
- read_excel (sheets)
- read_json
- read_sql
- parquet
- to_csv/to_excel with index=False
- encodings
- first look at the RetailMart tables
**SQL bridge:** COPY and \copy
**Common mistakes:** Index column on export; IDs read as numbers (lost zeros); wrong encoding
**Practice:** Load orders, customers and stores; inspect each

### Topic 37. Selecting: [], loc, iloc
**Goal:** Pick rows and columns exactly.
**Covers:**
- [] vs .loc vs .iloc
- label vs position slices (loc end is inclusive)
- several columns
- boolean rows
- .at/.iat
- selecting with an index
- MultiIndex intro
**SQL bridge:** SELECT columns, LIMIT
**Common mistakes:** Chained indexing; loc inclusive end; iloc out of range
**Practice:** Pick columns and row ranges from orders

### Topic 38. Filtering
**Goal:** Keep only the rows you need.
**Covers:**
- Boolean conditions
- & | ~ with brackets
- isin
- between
- str.contains
- query()
- isna
- combining filters
**SQL bridge:** WHERE, IN, BETWEEN, LIKE
**Common mistakes:** Using and/or; missing brackets; NaN comparisons
**Practice:** Delivered orders above ₹1 lakh in one city

### Topic 39. Sorting, head, unique
**Goal:** Rank and summarise values.
**Covers:**
- sort_values (several keys)
- sort_index
- nlargest/nsmallest
- head/tail
- unique/nunique
- value_counts (normalize)
- duplicated preview
- sample
**SQL bridge:** ORDER BY, LIMIT, DISTINCT
**Common mistakes:** Sorting strings that look like numbers; forgetting ascending list
**Practice:** Top 10 customers by spend

### Topic 40. New columns
**Goal:** Create derived columns the vectorised way.
**Covers:**
- Assigning columns
- assign()
- vectorised arithmetic
- apply (row/column)
- map and replace
- np.where and np.select
- clip
- round
- vectorised vs apply speed
**SQL bridge:** Derived columns and CASE
**Common mistakes:** Using apply when a vectorised form exists; SettingWithCopy; axis=1 slowness
**Practice:** Margin %; discount tier

### Topic 41. Missing values
**Goal:** Find, understand and treat missing data.
**Covers:**
- isna/notna
- counting
- dropna (how, subset)
- fillna (value, ffill, bfill)
- interpolate
- replacing placeholders
- NaN vs None vs pd.NA
- effect on aggregates
**SQL bridge:** NULL handling, COALESCE
**Common mistakes:** NaN != NaN; dropping too much; filling before splitting data
**Practice:** Missing report; sensible fills per column

### Topic 42. Data types & casting
**Goal:** Get dtypes right.
**Covers:**
- dtypes
- astype
- to_numeric(errors='coerce')
- to_datetime
- category
- nullable dtypes (Int64)
- memory_usage
- downcasting
- object columns
**SQL bridge:** CAST and ::
**Common mistakes:** IDs as floats; mixed object columns; silent coercion
**Practice:** Fix types of a messy table

### Topic 43. String & date accessors
**Goal:** Clean text and dates in whole columns.
**Covers:**
- .str (lower, strip, split, contains, replace, extract, len)
- .dt (year, month, dayofweek, strftime, normalize)
- Timedelta
- Period
- mixed date formats
**SQL bridge:** String and date functions
**Common mistakes:** Forgetting .str; regex=True defaults; timezone-naive vs aware
**Practice:** Clean city names; order month and weekday

## Module 3: Analysis with pandas

**Outcome:** Answer business questions: group, pivot, join, rank, clean and summarise.
**Time:** about 24 h

### Topic 44. groupby & aggregation
**Goal:** Split-apply-combine.
**Covers:**
- groupby
- agg (sum, mean, count, nunique)
- several aggregations
- named aggregation
- several keys
- as_index
- size vs count
- transform
- filter
- reset_index
**SQL bridge:** GROUP BY and HAVING
**Common mistakes:** count vs size; NaN keys dropped; forgetting reset_index
**Practice:** Revenue by city and status

### Topic 45. Pivot tables & crosstab
**Goal:** Reshape summaries into grids.
**Covers:**
- pivot_table (values, index, columns, aggfunc, fill_value, margins)
- crosstab
- normalize
**SQL bridge:** Conditional aggregation with CASE
**Common mistakes:** Wrong aggfunc; NaN cells; duplicate index error in pivot()
**Practice:** Monthly revenue by category grid

### Topic 46. Reshaping: melt, stack, unstack
**Goal:** Move between wide and long.
**Covers:**
- melt
- pivot
- stack/unstack
- wide vs long
- flattening MultiIndex columns
- explode
**SQL bridge:** UNNEST, crosstab()
**Common mistakes:** Losing id_vars; MultiIndex confusion
**Practice:** Wide KPI table to long and back

### Topic 47. merge: all the JOINs
**Goal:** Combine tables correctly.
**Covers:**
- inner/left/right/outer
- on, left_on/right_on
- suffixes
- validate
- indicator
- many-to-many explosion
- merge on index
- join()
**SQL bridge:** INNER/LEFT/RIGHT/FULL JOIN
**Common mistakes:** Duplicate keys multiply rows; key dtype mismatch; lost rows with inner
**Practice:** Orders + stores + customers

### Topic 48. concat & anti-joins
**Goal:** Stack tables and find what never happened.
**Covers:**
- concat (axis, ignore_index, keys)
- anti-join with indicator or ~isin
- semi-join
- set operations via concat/drop_duplicates/merge
**SQL bridge:** UNION, EXCEPT, LEFT JOIN ... IS NULL
**Common mistakes:** Misaligned columns; forgetting ignore_index
**Practice:** Customers who never ordered

### Topic 49. Window-style: rank, cumsum, rolling
**Goal:** Running totals, ranks and moving averages.
**Covers:**
- rank (methods)
- cumsum/cumprod
- shift/diff/pct_change
- rolling and expanding
- ewm intro
- groupby + transform
- top-N per group
- month-on-month growth
**SQL bridge:** Window functions: ROW_NUMBER, RANK, LAG, SUM() OVER
**Common mistakes:** Wrong sort before shift; min_periods; rank ties
**Practice:** Running revenue; MoM growth; top 3 products per category

### Topic 50. Duplicates & cleaning
**Goal:** Make dirty data trustworthy.
**Covers:**
- duplicated/drop_duplicates (subset, keep)
- standardising text
- fixing types
- trimming
- replace
- validation checks and assert
- a data-quality report
**SQL bridge:** ROW_NUMBER de-duplication
**Common mistakes:** Dropping the wrong duplicate; hidden whitespace
**Practice:** Clean a messy customer file

### Topic 51. Outliers & binning
**Goal:** Spot extremes and make buckets.
**Covers:**
- IQR and z-score
- clip/winsorise
- cut and qcut
- custom bins and labels
- value_counts on bins
**SQL bridge:** WIDTH_BUCKET, NTILE
**Common mistakes:** Deleting valid extremes; qcut with duplicate edges
**Practice:** Order-value bands; flag outliers

### Topic 52. Time series with pandas
**Goal:** Analyse data over time.
**Covers:**
- DatetimeIndex
- resample (D, W, M, Q)
- rolling on time
- shift by frequency
- date_range
- asfreq
- filling missing dates
- year-on-year
- seasonality intro
**SQL bridge:** generate_series gap filling, DATE_TRUNC
**Common mistakes:** Unsorted index; missing periods; resample on a non-index column
**Practice:** Monthly revenue; fill missing days

### Topic 53. Subtotals & percent of total
**Goal:** Totals, shares and Pareto.
**Covers:**
- groupby + transform('sum')
- pivot margins
- ROLLUP-style subtotals
- cumulative %
- the 80/20 rule
- share of total
**SQL bridge:** ROLLUP, CUBE, GROUPING SETS
**Common mistakes:** Percent of the wrong total; rounding sums
**Practice:** Category share; top customers making 80% of revenue

### Topic 54. describe, quantiles & correlation
**Goal:** Summarise distributions and relationships.
**Covers:**
- describe
- quantile
- mean/median/mode/std
- skew intro
- corr/cov
- correlation vs causation
- groupby describe
**SQL bridge:** PERCENTILE_CONT, CORR
**Common mistakes:** Correlation read as causation; Pearson on skewed data
**Practice:** Profile the orders table

### Topic 55. Performance
**Goal:** Make pandas code fast enough.
**Covers:**
- timeit
- vectorise vs apply vs loops
- memory usage
- downcasting
- category
- chunked read_csv
- usecols
- parquet
- avoiding copies
- profiling basics
**SQL bridge:** Indexes and EXPLAIN as analogies
**Common mistakes:** Premature optimisation; chained copies; reading everything when a slice is needed
**Practice:** Speed up a slow cleaning script

## Module 4: Visualisation & Storytelling

**Outcome:** Choose the right chart, build it and tell the story.
**Time:** about 14 h

### Topic 56. matplotlib basics
**Goal:** Draw the standard charts.
**Covers:**
- Figure and Axes
- pyplot vs object-oriented
- line, bar, barh, hist, scatter, pie (and why to avoid it)
- show
- notebooks
**SQL bridge:** Charts from query results
**Common mistakes:** Mixing pyplot state and Axes; forgetting to sort bars
**Practice:** Revenue by city bar chart

### Topic 57. Customising charts
**Goal:** Make charts clean and shareable.
**Covers:**
- Titles, labels, ticks, legends
- colours and styles
- subplots and gridspec
- figsize
- annotations
- saving (png, svg, pdf, dpi)
- ₹ lakh/crore axis formatting
**SQL bridge:** Formatting with TO_CHAR
**Common mistakes:** Overlapping labels; saving a blank figure
**Practice:** Two-panel revenue and orders figure

### Topic 58. Choosing the right chart
**Goal:** Match the question to the chart.
**Covers:**
- Comparison, trend, distribution, relationship, composition
- misleading charts
- small multiples
- colour accessibility
**SQL bridge:** Choosing the right GROUP BY
**Common mistakes:** Truncated axes; 3D and pie overuse
**Practice:** Redraw 3 bad charts

### Topic 59. seaborn
**Goal:** Statistical charts in few lines.
**Covers:**
- Themes
- histplot/kdeplot
- boxplot/violinplot
- scatterplot/regplot
- barplot with intervals
- heatmap (correlations)
- pairplot
- countplot
- catplot/FacetGrid
- palettes
**SQL bridge:** Distribution queries
**Common mistakes:** Unreadable heatmaps; overplotting
**Practice:** Correlation heatmap; distribution by group

### Topic 60. plotly: interactive charts
**Goal:** Make charts people can explore.
**Covers:**
- plotly express line/bar/scatter/histogram
- hover
- facets
- export HTML
- when to use interactive charts
**SQL bridge:** Dashboards on top of SQL
**Common mistakes:** Huge interactive figures; exporting without data
**Practice:** Interactive revenue explorer

### Topic 61. Dashboard-style summaries
**Goal:** Build a one-page summary.
**Covers:**
- KPI table
- multi-panel figure
- small multiples
- sparklines
- conditional formatting with Styler
- summary tables
**SQL bridge:** KPI queries
**Common mistakes:** Too many metrics; no clear headline
**Practice:** One-page store scorecard

### Topic 62. Reporting to Excel & storytelling
**Goal:** Deliver results people can use.
**Covers:**
- to_excel with xlsxwriter/openpyxl
- formatting
- several sheets
- charts in Excel
- narrative structure (setup, insight, action)
- a one-slide summary
**SQL bridge:** Exporting query results
**Common mistakes:** Hard-coded numbers; unformatted exports
**Practice:** Weekly report workbook with a summary

## Module 5: Analyst Toolkit

**Outcome:** Use Python for the work analysts actually do beyond tables.
**Time:** about 18 h

### Topic 63. Data preprocessing
**Goal:** Prepare data for modelling.
**Covers:**
- Scaling (standard, min-max)
- encoding (one-hot, ordinal)
- train/test split
- data leakage
- outliers
- class imbalance (mention)
- a first sklearn pipeline
**SQL bridge:** Feature columns in SQL
**Common mistakes:** Fitting scalers on all data (leakage); one-hot explosion
**Practice:** Prepare orders for a model (bridge to the ML course)

### Topic 64. SQL from Python
**Goal:** Query databases from code.
**Covers:**
- sqlite3 basics
- parameterised queries and SQL injection
- pandas read_sql and to_sql
- SQLAlchemy engine
- connecting to PostgreSQL
- when to use SQL vs pandas
**SQL bridge:** Everything from the SQL course, called from Python
**Common mistakes:** String-formatting SQL; leaving connections open
**Practice:** Run RetailMart queries from Python

### Topic 65. Cohort & RFM
**Goal:** Retention and customer segments.
**Covers:**
- Cohort month
- retention table
- RFM scoring with qcut
- segments
- interpreting and acting
**SQL bridge:** Cohort and RFM from the SQL practice banks
**Common mistakes:** Cohort by the wrong date; scoring direction for recency
**Practice:** Retention heatmap; RFM segments

### Topic 66. Funnels
**Goal:** Where do users drop off?
**Covers:**
- Stages
- conversion and drop-off
- per-channel funnels
- time to convert
**SQL bridge:** Conversion funnels in SQL
**Common mistakes:** Counting events, not users; out-of-order stages
**Practice:** Order funnel by channel

### Topic 67. A/B testing basics
**Goal:** Decide if a difference is real.
**Covers:**
- Hypotheses
- p-value
- t-test
- chi-square
- sample size basics
- peeking and multiple tests
- scipy.stats
- effect size
**SQL bridge:** Aggregates per variant
**Common mistakes:** Stopping early; ignoring sample size; p-value misread
**Practice:** Test a discount campaign

### Topic 68. Automating a report
**Goal:** Turn analysis into a repeatable script.
**Covers:**
- Script structure
- functions
- main guard
- argparse
- configuration
- logging
- scheduling (cron, Task Scheduler)
- email-ready outputs
**SQL bridge:** Scheduled queries
**Common mistakes:** Hard-coded paths; no logging
**Practice:** Weekly sales report script

### Topic 69. APIs with requests
**Goal:** Pull data from web services.
**Covers:**
- HTTP basics
- GET and params
- JSON
- status codes
- keys and secrets safety
- rate limits
- pagination
- error handling
- saving results
- browser note (CORS)
**SQL bridge:** External tables
**Common mistakes:** Committing keys; ignoring status codes
**Practice:** Fetch and tabulate a public API

### Topic 70. Web scraping basics
**Goal:** Collect public data responsibly.
**Covers:**
- robots.txt, ethics and terms
- requests + BeautifulSoup
- selectors
- pd.read_html
- polite scraping
**SQL bridge:** n/a
**Common mistakes:** Scraping against terms; brittle selectors
**Practice:** Scrape one public table

### Topic 71. Jupyter best practices & project structure
**Goal:** Keep analysis reproducible.
**Covers:**
- Notebook hygiene
- restart and run all
- folders (data, src, notebooks, outputs)
- requirements.txt
- README
- reproducibility
- notebooks to scripts
**SQL bridge:** Versioned SQL scripts
**Common mistakes:** Out-of-order cells; hidden state
**Practice:** Restructure a messy notebook

## Module 6: Interview Prep & Capstone

**Outcome:** Be ready for analyst Python interviews and finish a portfolio project.
**Time:** about 16 h

### Topic 72. Core Python interview patterns
**Goal:** Solve the standard questions.
**Covers:**
- Reverse, palindrome, anagram, two-sum, frequency, de-duplicate, flatten, FizzBuzz
- two pointers
- sliding window intro
- Big-O of list/dict/set operations
- == vs is
- shallow vs deep copy
- generators
- decorators
- mutable default trap
**SQL bridge:** SQL interview patterns
**Common mistakes:** Explaining without complexity; off-by-one
**Practice:** 20 timed problems

### Topic 73. pandas interview patterns
**Goal:** Solve the standard data tasks.
**Covers:**
- Top-N per group
- running totals
- retention
- de-duplicate
- pivot
- merge pitfalls
- apply vs vectorise
- NaN handling
- second-highest
- df.copy and SettingWithCopy
- transform vs agg
**SQL bridge:** SQL window and join interview questions
**Common mistakes:** Row-by-row thinking; forgetting to reset_index
**Practice:** 20 timed tasks

### Topic 74. SQL vs pandas side by side
**Goal:** Move fluently between the two.
**Covers:**
- 30 tasks solved both ways
- performance trade-offs
- when to use which
**SQL bridge:** The whole SQL course
**Common mistakes:** Pulling millions of rows into pandas
**Practice:** Translate 15 queries both directions

### Topic 75. Algorithms basics
**Goal:** Know the basics interviewers expect.
**Covers:**
- Linear and binary search
- bubble, selection, insertion, merge and quick sort (concepts)
- Big-O
- recursion vs iteration
- stacks, queues and hash tables in use
**SQL bridge:** n/a
**Common mistakes:** Binary search off-by-one; unstable assumptions
**Practice:** 10 classic problems

### C. Capstone: RetailMart analysis end to end
**Goal:** Deliver a portfolio-grade analysis.
**Covers:**
- Frame the question
- load and clean
- analyse
- visualise
- recommend
- present
**SQL bridge:** A real business question across RetailMart
**Common mistakes:** Analysis without a decision; no README
**Practice:** Notebook + 1-page summary + GitHub repo

## Not on this site (own courses on the path)
Maths, classical and advanced ML, deep learning, NLP, computer vision, MLOps. Left out on purpose: Tkinter, Turtle, Django, MySQL/MongoDB drivers.

## How content gets prepared (next step)
1. Ali approves this curriculum (or edits `tools/curriculum_data.py`).
2. Per topic, in order: a content file in `tools/topics/` (story, examples, mistakes, 8 practice questions, 5 interview questions) written in Ali's voice; build and verify; Ali reviews on the held page; publish.
3. Get started pages and the notes index are regenerated from this data.
4. Topic numbers are stable from here: change the data file, never renumber by hand.
