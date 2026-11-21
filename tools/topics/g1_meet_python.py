from deck_lib import *

META = dict(
    path="get-started/meet-python", title="Meet Python", tag="Get started · Part 1 of 5",
    desc="Get started, part 1 of 5: what Python is, a short history from 1989 to Python 3.15, Python 2 vs 3, and when to use Python, SQL or Excel.",
    mission_label="In this part", mission="learn what Python is, where it came from, and when an analyst reaches for it.",
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(agenda([("What Python is", ["A language for giving instructions", "Readable on purpose", "What people build with it"]),
                     ("Where it came from", ["Guido van Rossum, 1989", "Python 2 and Python 3", "Python today"]),
                     ("Python, SQL or Excel?", ["What each tool is best at", "Match the job to the tool", "What this course covers"])]))
    S.append(scene("What Python Is", head("Part 1 · What it is", "Python is a language for giving instructions to a computer",
        "You write short, readable lines. Python runs them. That is the whole idea.") + grid(3, [
        card("blue", "General-purpose", "<p>One language for analysis, automation, websites, science and AI. You are not locked into one job.</p>"),
        card("green", "Readable", "<p>Code looks close to plain English. <code>print('Hello')</code> does what it says.</p>"),
        card("purple", "Huge library of add-ons", "<p>Other people's tools for tables (pandas), charts (matplotlib), databases, web data and machine learning. Free.</p>"),
    ]) + '<div style="margin-top:20px">' + cell("print('Hello, TheShiraverse')\nprint(2 + 3)\nprint('Rs', 499 * 2)") + '</div>'
        + tip("This runs for real in your browser. Press Run, then change a word and run again.")))
    S.append(scene("A Short History", head("Part 2 · History", "From a Christmas project to the world's everyday language",
        "Facts below are from the official Python FAQ and python.org.") +
        '<div class="timeline">'
        '<div class="row"><div class="when">Dec 1989</div><div>Guido van Rossum starts writing Python during the Christmas holidays.</div></div>'
        '<div class="row"><div class="when">Feb 1991</div><div>After just over a year of work, Guido posts the first public release to USENET.</div></div>'
        '<div class="row"><div class="when">2000</div><div>Python 2.0 is released.</div></div>'
        '<div class="row"><div class="when">Dec 2008</div><div>Python 3.0 arrives: a cleaner language that is not fully compatible with Python 2.</div></div>'
        '<div class="row"><div class="when">1 Jan 2020</div><div>Python 2 is officially retired: no more fixes, ever.</div></div>'
        '<div class="row"><div class="when">Oct 2026</div><div>Python 3.15 is the latest release (3.15.2 on 25 Oct 2026).</div></div></div>'
        + tip("The name is not the snake. Guido was reading scripts from <b>Monty Python's Flying Circus</b>, a 1970s BBC comedy, and wanted a name that was short, unique and a little mysterious.")))
    S.append(scene("Who Looks After Python", head("Part 2 · History", "Who looks after Python today") + grid(2, [
        card("blue", "The Python Software Foundation", "<p>An independent non-profit that holds the copyright on Python 2.1 and newer and works to promote and protect the language.</p>"),
        card("green", "Free and open source", "<p>You can use Python for work, study or business at no cost. Anyone can read its source code and propose improvements.</p>"),
    ]) + '<div style="margin-top:20px">' + cell("import sys\nprint('Major version running here:', sys.version_info.major)\nprint(sys.version_info.major >= 3)") + '</div>'
        + warn("Always learn and use <b>Python 3</b>. If a tutorial shows <code>print 'hello'</code> without brackets, it is Python 2 and out of date.")))
    S.append(scene("Python 2 vs Python 3", head("Part 2 · History", "Why Python 2 vs 3 still matters", "Old tutorials and old code on the internet are often Python 2. Spot them quickly.") +
        table(["", "Python 2 (retired)", "Python 3 (use this)"], [
            ["print", "<code>print 'hi'</code> (a statement)", "<code>print('hi')</code> (a function)"],
            ["7 / 2", "gives <code>3</code> (whole-number division)", "gives <code>3.5</code>; use <code>7 // 2</code> for 3"],
            ["Text", "bytes by default, Unicode separate", "Unicode text by default"],
            ["Support", "ended 1 Jan 2020", "actively maintained"]]) +
        '<div style="margin-top:20px">' + cell("print(7 / 2)\nprint(7 // 2)") + '</div>'))
    S.append(scene("Why Analysts Use Python", head("Part 3 · Python, SQL or Excel?", "Three tools, three strengths",
        "You will use all three. The skill is knowing which to reach for.") + grid(3, [
        card("green", "Excel", "<p>Fast for small data, quick what-ifs and sharing with people who live in spreadsheets. Hard to repeat and audit at scale.</p>"),
        card("blue", "SQL", "<p>Best for asking questions of data that lives in a database: filter, join, group. The work happens where the data is.</p>"),
        card("purple", "Python", "<p>Best for cleaning messy files, repeating work every week, statistics, charts and anything the other two cannot do. It can also run SQL.</p>"),
    ]) + tip("In this course every Python topic points back to the SQL idea you already know, so you are translating, not starting over.")))
    S.append(scene("Match the Job", head("Part 3 · Python, SQL or Excel?", "Which tool would you reach for?", "Think first, then click to check.") + grid(2, [
        reveal("Total sales by city from a database with 20 lakh rows", "<b>SQL.</b> The data lives in the database, and <code>GROUP BY</code> runs right there."),
        reveal("A quick what-if on 30 rows to show your manager", "<b>Excel.</b> Small, visual, and your manager can open it."),
        reveal("Clean 50 messy CSV files the same way every Monday", "<b>Python.</b> Write the steps once, run them every week."),
        reveal("Join three tables and filter by date", "<b>SQL</b> if they are in a database. <b>pandas</b> (Python) if they are files."),
        reveal("Run a statistical test and draw a chart for a report", "<b>Python.</b> Libraries for statistics and charts are its home ground."),
        reveal("Call a web service and save the JSON it returns", "<b>Python.</b> SQL and Excel cannot do this well."),
    ])))
    S.append(scene("What This Course Covers", head("Part 3 · Python, SQL or Excel?", "What you will be able to do", "Six modules, topic by topic. No calendar: move at your own speed.") + table(["Module", "You will learn"], [
        ["1 Python Foundations", "values, text, lists, dictionaries, loops, functions, files, errors, small classes"],
        ["2 NumPy &amp; pandas Basics", "load, inspect, select, filter and clean tables"],
        ["3 Analysis with pandas", "group, pivot, join, rank, time series, summaries"],
        ["4 Visualisation", "the right chart, built well, with a story"],
        ["5 Analyst Toolkit", "SQL from Python, cohorts, funnels, A/B tests, automation"],
        ["6 Interview Prep &amp; Capstone", "interview patterns and a portfolio project"]]) +
        tip("Machine learning, deep learning and maths are separate courses on TheShiraverse path. This one gets you ready for them.")))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these?", "Click a card to check yourself.") + grid(3, [
        reveal("Who created Python, and roughly when?", "Guido van Rossum, started in December 1989; first public release February 1991."),
        reveal("Where does the name come from?", "The comedy series Monty Python's Flying Circus, not the snake."),
        reveal("Which version do you learn?", "Python 3. Python 2 was retired on 1 January 2020."),
        reveal("What does <code>7 / 2</code> give in Python 3?", "<code>3.5</code>. Use <code>7 // 2</code> for 3."),
        reveal("Name one job where Python beats SQL and Excel.", "Cleaning many files the same way every week, or calling a web service."),
        reveal("Does Python replace SQL?", "No. They work together; Python can even run SQL queries."),
    ])))
    S.append(closing("How Python runs", "/notes/get-started/how-python-runs/", "What happens between writing a line of code and seeing the result: the interpreter, scripts, notebooks and the REPL."))
    return S
