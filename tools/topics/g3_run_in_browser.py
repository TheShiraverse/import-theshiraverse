from deck_lib import *

META = dict(
    path="get-started/run-in-your-browser", title="Run Python in Your Browser", tag="Get started · Part 3 of 5",
    desc="Get started, part 3 of 5: run, edit and re-run Python in your browser with no install, use the playground, and know what works here and what needs your laptop.",
    mission_label="In this part", mission="run real Python in this page, and know exactly what works in the browser and what does not.",
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(agenda([("How it works", ["Python inside your browser tab", "What the first run does", "Your code stays on your device"]),
                     ("Using the cells and playground", ["Run, edit, reset, copy", "Each cell starts fresh", "The playground remembers"]),
                     ("Limits", ["What works here", "What needs your laptop", "Try it: five small tasks"])]))
    S.append(scene("How It Works", head("Part 1 · How it works", "Real Python, running in your browser tab",
        "The interpreter you met in the last part has been compiled so it runs inside the browser. No install, no account, works on a phone too.") + grid(3, [
        card("blue", "First run", "<p>The first time you press Run, the browser downloads Python (about 10 MB). You will see a message. After that it is fast.</p>"),
        card("green", "On your device", "<p>The code runs on your computer or phone, in your tab. Nothing you type is sent to a server to be run.</p>"),
        card("purple", "Same language", "<p>It is genuine Python 3, so what you learn here is what you will use on your laptop.</p>"),
    ]) + '<div style="margin-top:20px">' + cell("print('Running inside the browser')\nimport sys\nprint('Python', sys.version_info.major)") + '</div>'))
    S.append(scene("Using a Cell", head("Part 2 · Using the cells", "Every code box on this site is a live cell", "Run it, change it, break it. You cannot hurt anything.") +
        grid(2, [cell("name = 'TheShiraverse'\ngreeting = 'Hello, ' + name\nprint(greeting)", vars=True),
                 '<div class="card"><span class="k">Controls</span><ul style="padding-left:18px;color:var(--muted);line-height:1.9"><li><b>Run</b> or <b>Ctrl/Cmd + Enter</b> runs the cell</li><li>Click in the box and <b>edit</b> the code</li><li><b>Reset</b> restores the original code</li><li><b>Copy</b> copies it so you can paste it elsewhere</li><li>The <b>memory table</b> shows the variables the cell created</li><li><b>Tab</b> inserts four spaces</li></ul></div>'])))
    S.append(scene("Each Cell Starts Fresh", head("Part 2 · Using the cells", "In the notes, every cell starts from a clean slate",
        "A variable made in one cell is not visible in the next. That keeps every example self-contained.") +
        grid(2, ['<div><div class="label g">Cell A: makes a variable</div>' + cell("secret = 42\nprint(secret)") + '</div>',
                 '<div><div class="label r">Cell B: tries to use it</div>' + cell("print(secret)", raises="NameError") + '</div>']) +
        tip("The playground is different: it <b>remembers</b> variables from one run to the next, like a notebook. Use it when you want to build on earlier lines.")))
    S.append(scene("The Playground", head("Part 2 · Using the playground", "A blank page to experiment on",
        "Open <a href=\"/playground/\">python.theshiraverse.com/playground</a>. It loads pandas and NumPy and ten RetailMart tables so you can try real data early.") + grid(3, [
        card("blue", "Examples menu", "<p>Pick a starter: hello, reading a table, filtering, grouping, merging.</p>"),
        card("green", "Remembers state", "<p>Variables stay between runs, so you can build step by step.</p>"),
        card("purple", "Table list", "<p>The left panel lists each RetailMart file with its columns. Read one with <code>pd.read_csv('data/sales.orders.csv')</code>.</p>"),
    ]) + warn("The playground is a quick taste. Real practice happens on your own laptop (part 4 sets it up).")))
    S.append(scene("What Works and What Does Not", head("Part 3 · Limits", "Know the edges so nothing surprises you") + grid(2, [
        card("green", "Works in the browser", "<ul><li>All core Python: values, text, lists, dictionaries, loops, functions, classes</li><li>Standard library: <code>math</code>, <code>random</code>, <code>datetime</code>, <code>json</code>, <code>re</code>, <code>csv</code></li><li>pandas and NumPy (in the playground)</li><li>Files, held in the browser's memory while the tab is open</li></ul>"),
        card("red", "Needs your laptop", "<ul><li><code>input()</code>: browser cells cannot wait for typing</li><li>Files that survive after you close the tab</li><li>Installing extra packages with pip</li><li>Heavy libraries such as deep-learning toolkits</li><li>Some web requests, which browsers block for safety</li></ul>"),
    ])))
    S.append(scene("Two Limits, Live", head("Part 3 · Limits", "See the two limits you will hit first") + grid(2, [
        '<div><div class="label g">Files live in memory</div>' + cell("with open('/tmp/note.txt', 'w') as f:\n    f.write('hello')\nprint(open('/tmp/note.txt').read())") + '</div>',
        '<div><div class="label r">input() cannot wait for a keyboard</div>' + cell("name = input('Your name? ')\nprint('Hi', name)", raises="*") + '</div>']) +
        tip("The file above vanishes when you close the tab. The <code>input()</code> error is expected here; you will learn <code>input()</code> properly in the Input &amp; output topic.")))
    S.append(scene("Try It: Five Small Tasks", head("Part 3 · Try it", "Run each one, then change it", "Each task is a cell. Edit, run, and see what changes.") + grid(2, [
        '<div class="card"><span class="k">1 · Change the greeting</span><p>Make it say your name.</p></div>' + cell("print('Hello, world')"),
        '<div class="card"><span class="k">2 · Change the numbers</span><p>Try a bigger multiplication.</p></div>' + cell("print(12 * 34)"),
        '<div class="card"><span class="k">3 · Fix the error</span><p>One word is misspelled.</p></div>' + cell("pritn('fix me')", raises="NameError"),
        '<div class="card"><span class="k">4 · Predict first</span><p>What will this print? Then run it.</p></div>' + cell("print('ha' * 3)"),
        '<div class="card"><span class="k">5 · Make your own</span><p>Create two variables and print their sum.</p></div>' + cell("a = 5\nb = 7\n", vars=True),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these?", "Click a card to check yourself.") + grid(3, [
        reveal("Where does the code actually run?", "On your own device, inside the browser tab."),
        reveal("Why does Cell B fail after Cell A?", "In the notes every cell starts fresh, so <code>secret</code> does not exist there."),
        reveal("Which tool remembers variables between runs?", "The playground."),
        reveal("Name one thing that needs your laptop.", "<code>input()</code>, files that last, pip installs, heavy libraries."),
        reveal("What happens to a file you write in the browser?", "It lives in memory and disappears when you close the tab."),
        reveal("How do you restore a cell you changed?", "Press Reset."),
    ])))
    S.append(closing("Set up Python on your laptop", "/notes/get-started/set-up-python/", "Install Python and VS Code, create a virtual environment, install packages with pip, and run Jupyter."))
    return S
