from deck_lib import *

META = dict(
    module=1, num=1, slug="hello-python", title="Hello Python",
    desc="Python Module 1, topic 1: write and run your first programs with print(), text in quotes, comments, indentation, the errors every beginner meets, and how to ask Python for help. Run every example in your browser.",
    mission="write and run your first programs, and read the errors Python gives you.",
    next=("Variables & Data Types", "variables-data-types"),
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(scene("Today's Agenda", head("Agenda", "What we cover today") + grid(3, [
        '<div class="pillar"><div class="n">01</div><h3>print() and text</h3><ul><li>Your first program</li><li>Several values, sep and end</li><li>Quotes and escapes</li></ul></div>',
        '<div class="pillar"><div class="n">02</div><h3>The shape of code</h3><ul><li>Comments</li><li>Statements and long lines</li><li>Indentation is syntax</li></ul></div>',
        '<div class="pillar"><div class="n">03</div><h3>Errors and help</h3><ul><li>Six errors you will meet</li><li>help() and dir()</li><li>PEP 8 and the Zen of Python</li></ul></div>',
    ])))
    S.append(scene("Story: The Receipt That Would Not Print", head("Main story", "The receipt that would not print",
        "Meera runs a small chai stall and wants a tablet to print a welcome line on every bill. She types it exactly as she would say it.") + grid(3, [
        card("blue", "The setup", "<p>She types <code>print(Welcome to Chai Corner)</code>. It looks right to her. It is what she wants to say.</p>"),
        card("red", "The bug", "<p>Python stops with an error. It does not see a sentence. It sees words it has never heard of, because nothing told it this is <b>text</b>.</p>"),
        card("green", "The fix", "<p>Text goes inside quotes. The moment she adds them, the line prints. Most first errors in Python are this small.</p>"),
    ]) + '<div style="margin-top:20px">' + cell("print('Welcome to Chai Corner')") + "</div>"))
    S.append(scene("How It Relates to SQL", head("Story → SQL", "You already know the idea from SQL",
        "SQL <code>SELECT</code> shows you a result. Python <code>print()</code> shows you output. A few habits change.") +
        '<div class="card"><table class="map"><tr><th>In SQL</th><th>In Python</th></tr>'
        "<tr><td><code>SELECT</code> shows a result</td><td><code>print()</code> shows output</td></tr>"
        "<tr><td>A statement ends with <code>;</code></td><td>A statement ends at the end of the line</td></tr>"
        "<tr><td>Text is <code>'single quoted'</code></td><td>Text is <code>'single'</code> or <code>\"double\"</code> quoted</td></tr>"
        "<tr><td>Comment: <code>-- note</code></td><td>Comment: <code># note</code></td></tr>"
        "<tr><td>Indentation is only style</td><td>Indentation is <b>part of the language</b></td></tr></table></div>"
        + tip("Keywords like SELECT do not care about case. Python is case-sensitive: <code>print</code> works, <code>Print</code> does not.")))

    S.append(scene("print(): Your First Program", head("Topic 1 · print()", "print() shows something on the screen",
        "Put what you want to show inside the brackets. Text goes in quotes, numbers do not. Run it and read the output below the cell.") +
        cell("print('Hello, Python!')\nprint('My first program')\nprint(2 + 3)") +
        tip("Every run starts at the top and goes down one line at a time. Change the text and run again: you cannot break anything.")))
    S.append(scene("print(): Several Values, sep and end", head("Topic 1 · print()", "Many values, one line, and how to join them",
        "Give print() several values separated by commas. It puts a space between them and a new line at the end. <code>sep</code> changes the gap, <code>end</code> changes the ending.") + grid(2, [
        cell("print('Chai', 20)\nprint('Chai', 'Samosa', 'Biscuit')\nprint('Chai', 'Samosa', sep=' | ')\nprint('Total', 55, sep=': ')", rows=5),
        cell("print('Loading', end='...')\nprint('done')\nprint('A', 'B', 'C', sep='-', end='!')\nprint()\nprint('new line')", rows=6),
    ]) + warn("<code>sep</code> and <code>end</code> must be written with their names. They always come after the values.")))
    S.append(scene("Text in Quotes", head("Topic 1 · Text", "Quotes tell Python: this is text",
        "Single or double quotes make no difference. Pick the one that avoids extra work when the text itself contains a quote.") + grid(2, [
        cell("print('single quotes')\nprint(\"double quotes\")\nprint(\"It's fine inside double quotes\")\nprint('She said \"hi\"')\nprint('It\\'s fine with a backslash too')", rows=6),
        cell("print('Line one\\nLine two')\nprint('Name:\\tChai')\nprint('''Triple quotes\nspan several lines''')\nprint('C:\\\\data')", rows=6),
    ]) + '<div class="card" style="margin-top:14px"><span class="k">Escapes</span><p><code>\\n</code> new line &nbsp;·&nbsp; <code>\\t</code> tab &nbsp;·&nbsp; <code>\\\\</code> one backslash &nbsp;·&nbsp; <code>\\\'</code> a quote. A backslash inside text says: the next character is special.</p></div>'))
    S.append(scene("Comments", head("Topic 1 · Comments", "A comment is a note for humans",
        "Anything after <code>#</code> on a line is ignored by Python. Use comments to say <b>why</b>, not to repeat what the code already says.") +
        cell("# Print the shop name\nprint('Chai Corner')   # a note at the end of a line\n# print('this line is switched off')\nprint('Open 7 am to 10 pm')", rows=5) +
        tip("Putting <code>#</code> in front of a line to switch it off is called commenting it out. It is the fastest way to test without deleting.")))
    S.append(scene("Statements and Long Lines", head("Topic 1 · Statements", "One statement per line, and how to split a long one",
        "Python reads one statement per line. There is no <code>;</code> to end it. When a line gets long, break it inside brackets, or end the line with a backslash.") + grid(2, [
        cell("total = 120 + 80 + 45 + \\\n        30\nprint(total)\n\nitems = ['chai',\n         'samosa',\n         'biscuit']\nprint(items)", rows=9),
        '<div class="card"><span class="k">Two ways to continue a line</span><ul style="padding-left:18px;color:var(--muted);line-height:1.9"><li><b>Inside brackets</b> <code>( ) [ ] { }</code>: just press Enter. This is the style most people prefer.</li><li><b>A backslash</b> <code>\\</code> as the very last character on the line.</li></ul><p style="color:var(--muted)">Variables and lists come in the next topics. Today only notice that one statement can span several lines.</p></div>',
    ])))
    S.append(scene("Indentation Defines Blocks", head("Topic 1 · Indentation", "In Python the spaces at the start of a line matter",
        "Other languages use braces or keywords to group lines. Python uses indentation. A line that ends with <code>:</code> opens a block, and the indented lines under it belong to it.") + grid(2, [
        cell("price = 120\nif price > 100:\n    print('Expensive')\n    print('Check the bill')\nprint('Done')", vars=False, rows=6),
        '<div class="card"><span class="k">Read it like this</span><ul style="padding-left:18px;color:var(--muted);line-height:1.9"><li>The first two lines with 4 spaces run <b>only if</b> the test is true.</li><li><code>print(\'Done\')</code> is back at the left edge, so it always runs.</li><li>Use <b>4 spaces</b> for each level, the standard.</li></ul><p style="color:var(--muted)"><code>if</code> is topic 8. Today just see the shape.</p></div>',
    ])))

    S.append(scene("Mistake: Forgetting Quotes", mistake("Common mistake", "Text without quotes is a name, not text",
        "Without quotes Python looks for a variable called <code>Hello</code>. It does not exist, so you get a <code>NameError</code>.",
        "print(Hello)", "NameError", "print('Hello')",
        "<code>NameError: name 'Hello' is not defined</code> means: you used a word Python has not been told about. Add quotes if you meant text.")))
    S.append(scene("Mistake: A Quote That Never Closes", mistake("Common mistake", "Every opening quote needs a closing quote",
        "Open a quote and forget to close it and Python reads on, looking for the end of the text. It never finds it.",
        "print('Welcome to Chai Corner)", "SyntaxError", "print('Welcome to Chai Corner')",
        "<code>SyntaxError</code> means Python could not even read the line. The message says the text never ended. Look at the quotes first.")))
    S.append(scene("Mistake: A Bracket That Never Closes", mistake("Common mistake", "Every opening bracket needs a closing bracket",
        "Brackets work in pairs. The error often appears on the <b>next</b> line, because Python was still waiting for the closing bracket.",
        "print('Total:', 250", "SyntaxError", "print('Total:', 250)",
        "<code>'(' was never closed</code> points at the bracket you opened. Count your brackets: opens must equal closes.")))
    S.append(scene("Mistake: print Without Brackets", mistake("Common mistake", "The Python 2 habit",
        "In old Python 2, <code>print 'Hello'</code> worked. In Python 3, print is a function, so it needs brackets. Old tutorials still show the old way.",
        "print 'Hello'", "SyntaxError", "print('Hello')",
        "Python 3 even suggests the fix: <code>Missing parentheses in call to 'print'. Did you mean print(...)?</code> When you copy old code, add the brackets.")))
    S.append(scene("Mistake: IndentationError", mistake("Common mistake", "A block needs an indented line under it",
        "A line ending with <code>:</code> promises a block. If the next line is not indented, or an unexpected line is indented, Python refuses.",
        "if True:\nprint('inside')", "IndentationError", "if True:\n    print('inside')",
        "<code>expected an indented block</code> means: add 4 spaces. <code>unexpected indent</code> means: remove spaces that should not be there.")))
    S.append(scene("Mistake: Tabs and Spaces Mixed", mistake("Common mistake", "Never mix tabs and spaces",
        "A tab and four spaces can look the same on screen but are different characters. Mixing them in one block gives a <code>TabError</code>.",
        "if True:\n    print('spaces')\n\tprint('a tab')", "TabError", "if True:\n    print('spaces')\n    print('also spaces')",
        "Set your editor to insert 4 spaces when you press Tab. VS Code does this for Python by default.")))

    S.append(scene("help() and dir()", head("Topic 1 · Asking Python", "Python can explain itself",
        "<code>help(name)</code> shows the built-in manual for something. <code>dir(value)</code> lists what a value can do. Together they are your offline documentation.") + grid(2, [
        '<div><div class="label g">help(len)</div>' + cell("help(len)", rows=2) + "</div>",
        '<div><div class="label g">What can text do?</div>' + cell("names = [n for n in dir('abc') if not n.startswith('_')]\nprint(len(names), 'things, for example:')\nprint(names[:6])", rows=4) + "</div>",
    ]) + tip("You do not need to understand every word in <code>help()</code> yet. Look for the first line: it tells you what the thing does.")))
    S.append(scene("PEP 8 and the Zen of Python", head("Topic 1 · Style", "Python has a style guide and a philosophy",
        "<b>PEP 8</b> is the official style guide: 4 spaces per indent, lines up to 79 characters, <code>snake_case</code> names, spaces around operators. <code>import this</code> prints the <b>Zen of Python</b>.") + grid(2, [
        cell("import sys\nsys.modules.pop('this', None)   # a module loads only once; this lets us print it again\nimport this", rows=4),
        '<div class="card"><span class="k">Three lines worth remembering</span><ul style="padding-left:18px;color:var(--muted);line-height:1.9"><li><b>Readability counts.</b> You read code far more than you write it.</li><li><b>Simple is better than complex.</b></li><li><b>Errors should never pass silently.</b> Read the message, it is trying to help.</li></ul></div>',
    ])))
    S.append(scene("Real World: A Receipt From print()", head("Real world", "A printed receipt, with nothing but print()",
        "Everything on this page, in one small program: text, several values, sep, a comment and a tidy layout.") +
        cell("# Receipt for Chai Corner\nprint('============================')\nprint('        CHAI CORNER')\nprint('============================')\nprint('Chai', 20, sep=' ........ ')\nprint('Samosa', 15, sep=' ... ')\nprint('----------------------------')\nprint('TOTAL', 35, sep=' : ')", rows=9) +
        tip("Typing every total by hand is the problem the next topic solves with variables, so the program can calculate it for you.")))

    P1 = [
        practice("Easy", "Print the receipt header <code>*** Chai Corner ***</code>.", "print()", "*** Chai Corner ***", "print('*** Chai Corner ***')"),
        practice("Easy", "Print <code>Chai</code> and <code>Samosa</code> on one line, separated by <code> | </code> (space, bar, space).", "print()", "Chai | Samosa", "print('Chai', 'Samosa', sep=' | ')"),
        practice("Medium", "Print <code>10 20 30</code> followed immediately by <code>!</code> on the same line. Use one print and <code>end</code>.", "print(10, 20, 30)", "10 20 30!", "print(10, 20, 30, end='!')"),
        practice("Medium", "Fix the broken line so it prints <code>Total: 250</code>.", "print('Total:', 250", "Total: 250", "print('Total:', 250)"),
    ]
    P2 = [
        practice("Hard", "Print <code>Item</code> on one line and <code>Chai</code> on the next, using <b>one</b> print call and <code>sep</code>.", "print()", "Item\nChai", "print('Item', 'Chai', sep='\\n')"),
        practice("Hard", "Fix this Python 2 habit so it prints <code>Total 250</code>.", "print 'Total', 250", "Total 250", "print('Total', 250)"),
        practice("Crazy", "Print exactly <code>She said \"hi\"</code> with the double quotes showing.", "print()", "She said \"hi\"", "print('She said \"hi\"')"),
        practice("Crazy", "One bracket is missing. Fix it so the sum, split over three lines, prints <code>600</code>.", "total = (100 +\n         200 +\n         300\nprint(total)", "600", "total = (100 +\n         200 +\n         300)\nprint(total)"),
    ]
    S.append(scene("Practice Arena: Easy and Medium", head("Practice Arena", "Easy and Medium", "Type the answer, press Run. Green means correct.") + grid(2, P1)))
    S.append(scene("Practice Arena: Hard and Crazy", head("Practice Arena", "Hard and Crazy", "Predict before you run. Fix the broken lines by reading the error.") + grid(2, P2)))

    S.append(scene("Interview Studio", head("Interview Studio", "Five questions asked on day one") + grid(2, [
        reveal("What changed about print between Python 2 and 3?", "In Python 2 it was a statement: <code>print 'x'</code>. In Python 3 it is a function and needs brackets: <code>print('x')</code>. The old form is a <code>SyntaxError</code> in Python 3."),
        reveal("What do sep and end do in print()?", "<code>sep</code> is what goes between values (default one space). <code>end</code> is what goes after the last value (default a new line)."),
        reveal("Is there a difference between 'single' and \"double\" quotes?", "No. Both make the same text. Choose the one that avoids a backslash, for example <code>\"It's\"</code>, and be consistent."),
        reveal("How does Python know where a block ends?", "By indentation. Lines indented the same amount under a <code>:</code> line form the block. The standard is 4 spaces. Mixing tabs and spaces gives a <code>TabError</code>."),
        reveal("How do you learn what an unfamiliar function does?", "<code>help(function)</code> shows its manual, and <code>dir(value)</code> lists what a value can do. The official docs go deeper."),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these without running code?", "Click a card to check yourself.") + grid(3, [
        reveal("What does <code>print('a', 'b', sep='-')</code> show?", "<code>a-b</code>"),
        reveal("What does <code>print(Hello)</code> raise?", "<code>NameError</code>. Without quotes, Hello is a name Python does not know."),
        reveal("What starts a comment?", "<code>#</code>. Python ignores the rest of the line."),
        reveal("Why does <code>print 'x'</code> fail?", "Python 3 needs brackets: <code>print('x')</code>."),
        reveal("How many spaces is one indent?", "4, by PEP 8."),
        reveal("What shows the Zen of Python?", "<code>import this</code>"),
    ])))
    S.append(scene("Key Takeaways", head("Key Takeaways", "Five rules to remember") + grid(3, [
        card("blue", "1 · print() shows output", "<p>Text in quotes, numbers without. <code>sep</code> and <code>end</code> shape the line.</p>"),
        card("green", "2 · Quotes make text", "<p>Single or double, both fine. Close every quote and every bracket.</p>"),
        card("orange", "3 · # is a comment", "<p>Write why, not what. Comment out a line to test without deleting.</p>"),
        card("red", "4 · Indentation is syntax", "<p>4 spaces per level. Never mix tabs and spaces.</p>"),
        card("purple", "5 · Read the last error line", "<p><code>SyntaxError</code>, <code>NameError</code>, <code>IndentationError</code> each say what is wrong.</p>"),
        card("blue", "6 · Python helps you", "<p><code>help()</code>, <code>dir()</code> and <code>import this</code> are always there.</p>"),
    ])))
    def qr(t, code): return f"<div><h3>{t}</h3>{cell(code)}</div>"
    S.append(scene("Quick Reference", head("Quick Reference", "Every syntax from today") + grid(3, [
        qr("Print", "print('Hello', 'world')"),
        qr("sep and end", "print('a', 'b', sep='-', end='!')"),
        qr("Quotes", "print(\"It's\", 'a \"quote\"')"),
        qr("Comment", "# a note\nprint('hi')   # another"),
        qr("Long line", "total = (1 +\n         2 +\n         3)\nprint(total)"),
        qr("Help", "help(len)"),
    ])))
    S.append(scene("Take-Home Challenge", head("Take-Home Challenge", "Your own receipt",
        "Use only <code>print()</code>. Then break it on purpose and read the error.") + grid(2, [
        '<div class="card"><ol style="padding-left:20px;color:var(--muted);line-height:1.9"><li>Print a header for a shop you know, with a line of <code>=</code> above and below.</li><li>Print three items with their prices on one line each, using <code>sep</code>.</li><li>Print a total line.</li><li>Add a comment above each part saying what it does.</li><li>Delete one closing quote, run it, and read the error. Then fix it.</li></ol></div>',
        cell("# your receipt here\n", rows=10),
    ])))
    import curriculum_data
    topics = [t["title"] for t in curriculum_data.MODULES[1]["topics"] if t["n"].isdigit()]
    j = "".join(f'<span class="{"here" if i == 0 else ("done" if i < 0 else "")}">{i+1}. {t}</span>' for i, t in enumerate(topics))
    S.append(scene("Your Python Journey", head("Your Python journey", "Module 1: Python Foundations", "You are here: topic 1 of 29.") + f'<div class="journey">{j}</div>'))
    S.append(scene("Next: Variables & Data Types", head("Next topic", "Variables & Data Types",
        "Give values a name, know their types, and convert between them safely. Your receipt will finally calculate its own total.") +
        '<div class="mission"><b>Before the next topic:</b> finish the take-home and try your receipt in the playground: <a href="/playground/">python.theshiraverse.com/playground</a></div>'
        '<div style="margin-top:20px"><a class="btn-next" href="/notes/module-1/variables-data-types/">Next: Variables &amp; Data Types &rarr;</a></div>'))
    return S
