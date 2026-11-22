from deck_lib import *

META = dict(
    module=1, num=4, slug="strings-text-basics", title="Strings 1: Text Basics",
    desc="Python Module 1, topic 4: quotes and escapes, joining and repeating text, len, indexing, negative indexing and slicing, why strings cannot be changed, and the errors that follow. Run every example in your browser.",
    mission="slice, index and inspect text: mask a card number, pull out an area code and reverse a word.",
    next=("Strings 2: Methods & Formatting", "strings-methods-formatting"),
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(scene("Today's Agenda", head("Agenda", "What we cover today") + grid(3, [
        '<div class="pillar"><div class="n">01</div><h3>Writing text</h3><ul><li>Quotes and escapes</li><li>Raw and triple-quoted text</li><li>Joining and repeating</li></ul></div>',
        '<div class="pillar"><div class="n">02</div><h3>Looking inside</h3><ul><li>len()</li><li>Indexing, also from the end</li><li>Slicing [start:stop:step]</li></ul></div>',
        '<div class="pillar"><div class="n">03</div><h3>Rules and traps</h3><ul><li>Strings never change</li><li>in and comparison</li><li>IndexError and off-by-one</li></ul></div>',
    ])))
    S.append(scene("Story: The Card Number in the Log", head("Main story", "The card number in the log",
        "A RetailMart support log prints the full 16-digit card number of a customer. The analyst is asked to share it with the vendor by evening.") +
        grid(3, [
            card("red", "The problem", '<p>Nobody outside the payments team should see all 16 digits. The vendor needs only the <b>last four</b> to match a complaint.</p>'),
            card("blue", "The idea", '<p>Text is a row of characters. Take the last four with a slice, and cover the rest with stars.</p>'),
            card("green", "The result", '<p>Three lines of Python turn the dangerous log line into a safe one.</p>'),
        ]) + '<div style="margin-top:20px">' + cell("card = '4111111111111111'\nlast4 = card[-4:]\nprint('*' * 12 + last4)") + '</div>'))
    S.append(scene("How It Relates to SQL", head("Story → SQL", "The same text tools, with different numbering",
        "SQL has text functions. Python does the same jobs with operators and brackets. The big difference: Python counts from <b>0</b>.") +
        table(["Job", "PostgreSQL", "Python"], [
            ["Length", "<code>LENGTH(s)</code>", "<code>len(s)</code>"],
            ["Join text", "<code>a || b</code>", "<code>a + b</code>"],
            ["Part of text", "<code>SUBSTRING(s FROM 1 FOR 3)</code> (starts at 1)", "<code>s[0:3]</code> (starts at 0)"],
            ["Contains", "<code>s LIKE '%abc%'</code>", "<code>'abc' in s</code>"],
            ["Last characters", "<code>RIGHT(s, 4)</code>", "<code>s[-4:]</code>"],
        ]) + warn("SQL's first character is position 1. Python's first character is index 0. Most beginner bugs in this topic come from that one difference.")))
    S.append(scene("Topic 1: Quotes and Escapes", head("Topic 1 · Writing text", "Single or double quotes, and the backslash",
        "Use either kind of quote. Pick the one that does not appear inside the text, or escape with a backslash.") + grid(2, [
            cell("print('Gwalior')\nprint(\"Gwalior\")\nprint(\"It's RetailMart\")\nprint('She said \"hello\"')\nprint('It\\'s fine too')"),
            cell("print('Line one\\nLine two')\nprint('Name\\tCity')\nprint('A backslash: \\\\')"),
        ]) + tip("<code>\\n</code> is a new line, <code>\\t</code> is a tab, <code>\\\\</code> is one real backslash.")))
    S.append(scene("Raw and Triple-Quoted Text", head("Topic 1 · Writing text", "r'' keeps backslashes, ''' ''' spans lines",
        "A raw string treats backslashes as plain characters. Triple quotes let one string run over many lines.") + grid(2, [
            cell("path = r'C:\\new\\table.csv'\nprint(path)\nprint(len(path))"),
            cell("note = '''Order 1\nShip to Gwalior\nCall before delivery'''\nprint(note)\nprint(len(note))"),
        ]) + tip("Triple-quoted text is also how you write long explanations (docstrings) in functions later.")))
    S.append(scene("Joining and Repeating", head("Topic 2 · Combining", "+ joins, * repeats",
        "Both make a <b>new</b> string. Numbers must be turned into text first with <code>str()</code>.") + grid(2, [
            cell("first = 'Samsung'\nmodel = 'Animi Max'\nprint(first + ' ' + model)\nprint('ab' * 3)\nprint('-' * 20)"),
            cell("order_id = 42\nprint('Order #' + str(order_id))\nprint('Total: ' + str(499.5))"),
        ]) + tip("A line of <code>'-' * 20</code> is the quickest way to draw a divider in printed output.")))
    S.append(scene("Topic 3: len() and Indexing", head("Topic 3 · Looking inside", "Every character has a position, starting at 0",
        "<code>len()</code> counts characters. <code>s[i]</code> gives the character at position <code>i</code>.") + grid(2, [
            cell("s = 'RetailMart'\nprint(len(s))\nprint(s[0])\nprint(s[1])\nprint(s[9])", vars=True),
            '<div class="card"><table class="map"><tr><th>R</th><th>e</th><th>t</th><th>a</th><th>i</th><th>l</th><th>M</th><th>a</th><th>r</th><th>t</th></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>-10</td><td>-9</td><td>-8</td><td>-7</td><td>-6</td><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr></table></div>',
        ]) + tip("The last valid index is always <code>len(s) - 1</code>.")))
    S.append(scene("Negative Indexing", head("Topic 3 · Looking inside", "-1 is the last character",
        "Negative numbers count from the end, so you never need to compute <code>len(s) - 1</code>.") +
        cell("s = 'RetailMart'\nprint(s[-1])\nprint(s[-2])\nprint(s[-10])\n\ncard = '4111111111111111'\nprint(card[-4])") +
        tip("<code>s[-1]</code> is the quickest way to get the last character: a file extension letter, a check digit, a last initial.")))
    S.append(scene("Topic 4: Slicing", head("Topic 4 · Slicing", "s[start:stop] takes a piece",
        "The slice <b>includes start and excludes stop</b>. Leave one out to go to the edge.") + grid(2, [
            cell("s = 'Samsung Animi Max'\nprint(s[0:7])\nprint(s[:7])\nprint(s[8:])\nprint(s[8:13])\nprint(s[-3:])"),
            '<div class="card"><p>Think of the numbers as <b>fences between characters</b>, not as the characters themselves.</p><p><code>s[0:7]</code> is everything between fence 0 and fence 7: the seven characters at positions 0 to 6.</p><p>That is why <code>s[:3] + s[3:]</code> always gives back the whole string.</p></div>',
        ])))
    S.append(scene("Slicing with a Step", head("Topic 4 · Slicing", "s[start:stop:step]",
        "The third number is the step. A step of <code>-1</code> walks backwards, so <code>[::-1]</code> reverses text.") +
        cell("s = 'Python'\nprint(s[::2])      # every second\nprint(s[1::2])\nprint(s[::-1])     # reversed\nprint(s[-1:-4:-1])\nprint('RetailMart'[::-1])") +
        tip("A slice never raises an error when it goes past the end. <code>'abc'[0:100]</code> is just <code>'abc'</code>.")))
    S.append(scene("Strings Cannot Be Changed", head("Topic 5 · Immutability", "Make a new string instead",
        "A string is <b>immutable</b>: once created, no character can be replaced in place. Every change builds a new string.") +
        cell("city = 'Gwalior'\nnew_city = 'B' + city[1:]\nprint(new_city)\nprint(city)       # the original is untouched\n\ncode = 'ORD-1'\ncode = code + '0'\nprint(code)", vars=True, rows=8) +
        tip("<code>code = code + '0'</code> does not change the old text. It creates a new string and moves the name <code>code</code> onto it.")))
    S.append(scene("Topic 6: in and Comparison", head("Topic 6 · Checking", "Does it contain? Is it equal? Which comes first?",
        "<code>in</code> tests for a piece of text. <code>==</code> compares the whole text. Comparison is case-sensitive.") + grid(2, [
            cell("s = 'Samsung Animi Max'\nprint('Animi' in s)\nprint('animi' in s)\nprint('xyz' not in s)\nprint('Samsung' == 'samsung')"),
            cell("print('apple' < 'banana')\nprint('Zebra' < 'apple')   # capitals come first\nprint('10' < '9')           # text, not numbers\nprint(ord('A'), ord('a'))"),
        ]) + warn("<code>'10' &lt; '9'</code> is <b>True</b>: text is compared character by character. Convert to numbers before comparing amounts.")))
    S.append(scene("Mistake: IndexError", mistake("Common mistake", "Asking for a position that does not exist",
        "The last index is <code>len(s) - 1</code>. Going one past it raises <code>IndexError</code>.",
        "s = 'RetailMart'\nprint(s[10])", "IndexError",
        "s = 'RetailMart'\nprint(s[9])\nprint(s[-1])\nprint(s[10:])",
        "Index with one position can fail; a slice never does. A slice past the end just gives an empty string.")))
    S.append(scene("Mistake: Changing a Character", mistake("Common mistake", "Item assignment on a string",
        "You cannot replace one character in place. Python says <code>'str' object does not support item assignment</code>.",
        "city = 'Gwalior'\ncity[0] = 'B'", "TypeError",
        "city = 'Gwalior'\ncity = 'B' + city[1:]\nprint(city)",
        "Build the new string from slices: the part before, the new piece, the part after.")))
    S.append(scene("Mistake: Off-by-One Slices", mistake("Common mistake", "The stop number is not included",
        "To take 3 characters starting at position 2 you need stop <code>5</code>, not 4. And the first character is <code>[0]</code>, not <code>[1]</code>.",
        "s = 'Samsung'\nprint(s[1:3])\nprint(s[1])", None,
        "s = 'Samsung'\nprint(s[0:3])\nprint(s[0])",
        "Count the wanted characters first: from index <code>a</code> taking <code>n</code> characters means <code>s[a : a + n]</code>.")))
    S.append(scene("Mistake: Backslashes in Windows Paths", mistake("Common mistake", "C:\\new\\table.csv is not what it looks like",
        "Inside normal quotes <code>\\n</code> is a new line and <code>\\t</code> is a tab. A Windows path silently changes.",
        "path = 'C:\\new\\table.csv'\nprint(path)\nprint(len(path))", None,
        "path = r'C:\\new\\table.csv'\nprint(path)\nprint(len(path))",
        "Use a raw string <code>r'...'</code> for Windows paths, or write forward slashes: <code>'C:/new/table.csv'</code> works too.")))
    S.append(scene("Real World: Mask a Card Number", head("Real world", "Hide all but the last four digits",
        "Combine slicing, repetition and <code>len()</code> so the mask fits any card length.") +
        cell("card = '4111111111111111'\nvisible = card[-4:]\nhidden = '*' * (len(card) - 4)\nprint(hidden + visible)\nprint(len(card))", vars=True) +
        tip("The star count comes from <code>len(card) - 4</code>, so the same code works for a 15-digit card too.")))
    S.append(scene("Real World: Pull Pieces Out of Codes", head("Real world", "Area code, order year and order number",
        "Fixed-format text is just fixed positions. Slice the position you need.") + grid(2, [
            cell("landline = '0751-2345678'\nprint(landline[:4])      # area code\nprint(landline[5:])      # number\nprint(landline[:4] + landline[5:])"),
            cell("code = 'ORD-2026-00042'\nprint(code[4:8])         # year\nprint(code[-5:])         # number as text\nprint(int(code[-5:]) + 1)   # next order"),
        ]) + tip("Slices give text. Wrap the piece in <code>int()</code> when you want to count with it.")))
    P1 = [
        practice("Easy", "Print the first word <code>Samsung</code> from <code>s</code> using a slice.", "s = 'Samsung Animi Max'\nprint()", "Samsung", "s = 'Samsung Animi Max'\nprint(s[:7])"),
        practice("Easy", "Print the number of characters in <code>'RetailMart'</code>.", "print()", "10", "print(len('RetailMart'))"),
        practice("Medium", "Mask the card: print 12 stars followed by its last four digits.", "card = '4111111111111111'\nprint()", "************1111", "card = '4111111111111111'\nprint('*' * 12 + card[-4:])"),
        practice("Medium", "Print the area code (first four characters) of the landline.", "landline = '0751-2345678'\nprint()", "0751", "landline = '0751-2345678'\nprint(landline[:4])"),
    ]
    P2 = [
        practice("Hard", "Reverse <code>'RetailMart'</code> with a slice and print it.", "print()", "traMliateR", "print('RetailMart'[::-1])"),
        practice("Hard", "Predict first, then print <code>s[1:4]</code>, <code>s[-3:]</code> and <code>s[::2]</code> on one line.", "s = 'Python'\nprint()", "yth hon Pto", "s = 'Python'\nprint(s[1:4], s[-3:], s[::2])"),
        practice("Crazy", "From the order code, print the order number plus one, as a number.", "code = 'ORD-2026-00042'\nprint()", "43", "code = 'ORD-2026-00042'\nprint(int(code[-5:]) + 1)"),
        practice("Crazy", "Print whether <code>word</code> reads the same backwards (a palindrome).", "word = 'level'\nprint()", "True", "word = 'level'\nprint(word == word[::-1])"),
    ]
    S.append(scene("Practice Arena: Easy and Medium", head("Practice Arena", "Easy and Medium", "Type the answer, press Run. Green means correct.") + grid(2, P1)))
    S.append(scene("Practice Arena: Hard and Crazy", head("Practice Arena", "Hard and Crazy", "Predict before you run. These are the traps interviewers like.") + grid(2, P2)))
    S.append(scene("Interview Studio", head("Interview Studio", "Five questions interviewers ask about strings") + grid(2, [
        reveal("Are Python strings mutable?", "No, they are immutable. <code>s[0] = 'x'</code> raises <code>TypeError</code>. You build a new string, for example <code>'x' + s[1:]</code>."),
        reveal("What does s[::-1] do?", "It slices the whole string with a step of -1, so it returns the string reversed."),
        reveal("What is the difference between s[5] and s[5:6]?", "<code>s[5]</code> raises <code>IndexError</code> if there is no position 5. <code>s[5:6]</code> never raises: it gives an empty string instead."),
        reveal("Why is '10' &lt; '9' True?", "Strings compare character by character. The first characters are <code>'1'</code> and <code>'9'</code>, and <code>'1'</code> comes first."),
        reveal("What is a raw string?", "A string with an <code>r</code> prefix, like <code>r'C:\\new'</code>. Backslashes are kept as plain characters, which is useful for Windows paths and patterns."),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these without running code?", "Click a card to check yourself.") + grid(3, [
        reveal("<code>'Python'[0]</code> and <code>'Python'[-1]</code>?", "<code>'P'</code> and <code>'n'</code>."),
        reveal("<code>'Python'[1:4]</code>?", "<code>'yth'</code>. Positions 1, 2, 3."),
        reveal("<code>len('Hello World')</code>?", "<code>11</code>. The space counts."),
        reveal("<code>'ab' * 3</code>?", "<code>'ababab'</code>."),
        reveal("<code>'abc'[5:]</code>?", "<code>''</code>, an empty string. Slices do not raise."),
        reveal("Can you do <code>s[0] = 'X'</code>?", "No. Strings are immutable: <code>TypeError</code>."),
    ])))
    S.append(scene("Key Takeaways", head("Key Takeaways", "Six rules to remember") + grid(3, [
        card("blue", "1 · Count from 0", '<p>First is <code>s[0]</code>, last is <code>s[-1]</code>. SQL starts at 1.</p>'),
        card("green", "2 · Stop is excluded", '<p><code>s[a:b]</code> takes positions a up to b-1.</p>'),
        card("orange", "3 · Step", '<p><code>s[::-1]</code> reverses. <code>s[::2]</code> takes every second.</p>'),
        card("red", "4 · Immutable", '<p>No in-place changes. Build a new string from slices.</p>'),
        card("purple", "5 · + and *", '<p><code>str()</code> before joining numbers. <code>"-" * 20</code> draws a line.</p>'),
        card("blue", "6 · Raw for paths", '<p><code>r"C:\\new"</code> keeps the backslashes.</p>'),
    ])))
    def qr(t, code): return f'<div><h3>{t}</h3>{cell(code)}</div>'
    S.append(scene("Quick Reference", head("Quick Reference", "Every syntax from today") + grid(3, [
        qr("Length and index", "s = 'RetailMart'\nprint(len(s), s[0], s[-1])"),
        qr("Slice", "s = 'RetailMart'\nprint(s[:6], s[6:], s[-4:])"),
        qr("Step and reverse", "s = 'RetailMart'\nprint(s[::2], s[::-1])"),
        qr("Join and repeat", "print('Order #' + str(42), '-' * 10)"),
        qr("Contains", "print('Mart' in 'RetailMart')"),
        qr("Raw string", "print(r'C:\\new\\table.csv')"),
    ])))
    S.append(scene("Take-Home Challenge", head("Take-Home Challenge", "A support log line",
        "A log line arrives as <code>'ORD-2026-00107 | 98765-43210 | 4111111111111111'</code>. Work in the cell below, then check against a classmate or in a 1:1.") + grid(2, [
        '<div class="card"><ol style="padding-left:20px;color:var(--muted);line-height:1.9"><li>Store the line in a variable.</li><li>Print its length.</li><li>Extract the order number (the last 5 digits of the code) as an integer.</li><li>Extract the mobile number and print its first five digits.</li><li>Print the card masked to its last four digits.</li><li>Print the whole line reversed.</li></ol></div>',
        cell("# your work here\nline = 'ORD-2026-00107 | 98765-43210 | 4111111111111111'\n", vars=True, rows=10),
    ])))
    import curriculum_data
    topics = [t["title"] for t in curriculum_data.MODULES[1]["topics"] if t["n"].isdigit()]
    j = "".join(f'<span class="{"here" if i == 3 else ("done" if i < 3 else "")}">{i+1}. {t}</span>' for i, t in enumerate(topics))
    S.append(scene("Your Python Journey", head("Your Python journey", "Module 1: Python Foundations", "You are here: topic 4 of 29.") + f'<div class="journey">{j}</div>'))
    S.append(scene("Next: Strings 2: Methods & Formatting", head("Next topic", "Strings 2: Methods &amp; Formatting",
        "Clean messy text and format it for printing: <code>upper</code>, <code>strip</code>, <code>split</code>, <code>replace</code> and f-strings.") +
        '<div class="mission"><b>Before the next topic:</b> finish the take-home and try it in the playground: <a href="/playground/">python.theshiraverse.com/playground</a></div>'
        '<div style="margin-top:20px"><span class="chip"><b>Next:</b> Strings 2: Methods &amp; Formatting (coming soon)</span></div>'))
    return S
