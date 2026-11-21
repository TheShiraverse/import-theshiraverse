from deck_lib import *

META = dict(
    path="get-started/how-python-runs", title="How Python Runs", tag="Get started · Part 2 of 5",
    desc="Get started, part 2 of 5: what happens when you press Run: the interpreter, bytecode, the REPL, scripts and notebooks, and how to read your first error.",
    mission_label="In this part", mission="see what happens between writing code and seeing output, and know the three ways to run Python.",
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(agenda([("The journey of a line", ["Interpreter in one picture", "Bytecode, peeked at", "Python versions"]),
                     ("Three ways to run Python", ["REPL: type and see", "Script: a .py file", "Notebook: cells and notes"]),
                     ("Output and errors", ["Reading what comes back", "Syntax errors vs runtime errors", "Your first traceback"])]))
    S.append(scene("From Code to Output", head("Part 1 · The journey", "What happens when you press Run",
        "Python is a program called the interpreter. It reads your code and does what it says, one step at a time.") +
        '<div class="flow"><div class="step"><b>1 Write</b>your code</div><div class="arrow">&rarr;</div>'
        '<div class="step"><b>2 Read</b>the interpreter checks the syntax</div><div class="arrow">&rarr;</div>'
        '<div class="step"><b>3 Translate</b>into bytecode, a compact set of steps</div><div class="arrow">&rarr;</div>'
        '<div class="step"><b>4 Run</b>the Python virtual machine does each step</div><div class="arrow">&rarr;</div>'
        '<div class="step"><b>5 Show</b>output or an error</div></div>'
        '<div style="margin-top:22px">' + cell("import platform\nprint('Interpreter:', platform.python_implementation())\nprint('Major version:', platform.python_version_tuple()[0])") + '</div>'
        + tip("SQL runs inside a database server. Python runs inside the interpreter, on your computer, or right here in your browser.")))
    S.append(scene("Peek at Bytecode", head("Part 1 · The journey", "Bytecode: the step you never see",
        "You never write bytecode, but you can look at it. Each line below is one small instruction.") +
        cell("import dis\n\ndef add(a, b):\n    return a + b\n\ndis.dis(add)") +
        tip("You do not need to read this. It shows that Python does not run your text directly; it first turns it into small steps.")))
    S.append(scene("Three Ways to Run Python", head("Part 2 · Three ways", "REPL, script or notebook", "Same language, three places to use it.") + grid(3, [
        card("blue", "REPL", "<p>Type a line, see the answer at once. Great for trying things. Nothing is saved. Start it with <code>python</code> or <code>python3</code> in a terminal.</p>"),
        card("green", "Script (.py)", "<p>A text file of code that runs top to bottom. Best for repeatable work and automation: <code>python report.py</code>.</p>"),
        card("purple", "Notebook (.ipynb)", "<p>Code in cells with notes and charts in between. Best for exploring data and sharing results. Jupyter and VS Code open them.</p>"),
    ]) + '<div style="margin-top:20px">' + table(["", "REPL", "Script", "Notebook"], [
        ["Saved?", "no", "yes", "yes, with output"], ["Best for", "quick tests", "automation", "analysis and stories"], ["Runs", "line by line", "start to end", "cell by cell"]]) + '</div>'))
    S.append(scene("The REPL Echo", head("Part 2 · Three ways", "In the REPL, the last value is shown for you",
        "Type an expression and Python prints its value. Our cells do the same for the last line.") +
        grid(2, [cell("2 + 3"), cell("'rupees ' * 3")]) +
        tip("In a script this echo does not happen. You must write <code>print(...)</code> to see anything.")))
    S.append(scene("Scripts and __name__", head("Part 2 · Three ways", "A script knows it is the main program",
        "Every file has a built-in name. When you run a file directly, that name is <code>__main__</code>.") +
        cell("print(__name__)") + warn("You will use this later (<code>if __name__ == '__main__':</code>) to let a file act as both a script and a module.")))
    S.append(scene("Python Versions", head("Part 3 · Versions and files", "A version is a number you should know",
        "Python 3.15 is the latest at the time of writing. Libraries state which Python versions they support.") + grid(2, [
        card("blue", "What a version number means", "<p><code>3.15.2</code> is major 3, minor 15, patch 2. Minor versions add features each year; patches fix bugs.</p>"),
        card("green", "Why it matters", "<p>Code written for 3.8 usually runs on 3.15, but new syntax from 3.15 will not run on old Pythons. Check with <code>python --version</code>.</p>"),
    ]) + '<div style="margin-top:20px">' + cell("import sys\nprint(sys.version_info.major, sys.version_info.minor)") + tip("The browser here runs Python 3.12, a little behind the latest. That is fine: everything in this course works on 3.12 and newer. Your laptop can have the newest version.") + '</div>'))
    S.append(scene("Reading Errors", head("Part 4 · Output and errors", "An error is information, not failure",
        "Python tells you what went wrong and where. Read the last line first.") + grid(2, [
        '<div><div class="label r">Runtime error: the code ran, then broke</div>' + cell("print(helo)", raises="NameError") + '</div>',
        '<div><div class="label r">Syntax error: Python cannot even start</div>' + cell("print('hello'", raises="SyntaxError") + '</div>',
    ]) + warn("A syntax error stops the program <b>before</b> anything runs. A runtime error happens <b>while</b> it runs, so earlier lines may already have printed.")))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these?", "Click a card to check yourself.") + grid(3, [
        reveal("What is the interpreter?", "The program that reads your code and runs it step by step."),
        reveal("REPL, script or notebook: which saves your work as a file of code?", "A script (.py). A notebook also saves, with its output."),
        reveal("In a script, why does <code>2 + 3</code> alone show nothing?", "Only the REPL and notebook cells echo the last value. In a script you need <code>print()</code>."),
        reveal("What does <code>__name__</code> equal when you run a file directly?", "<code>'__main__'</code>"),
        reveal("Which line of an error should you read first?", "The last line: it names the error and the reason."),
        reveal("Syntax error or runtime error: which happens before any code runs?", "A syntax error."),
    ])))
    S.append(closing("Run Python in your browser", "/notes/get-started/run-in-your-browser/", "Open the playground, run and change code, and learn what runs in the browser and what does not."))
    return S
