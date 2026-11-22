from deck_lib import *

META = dict(
    module=1, num=2, slug="variables-data-types", title="Variables & Data Types",
    desc="Python Module 1, topic 2: variables, int, float, str, bool and None, converting between types, and the three errors every beginner meets. Run every example in your browser.",
    next=("Numbers & Operators", "numbers-operators"),
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    # 2 agenda
    S.append(scene("Today's Agenda", head("Agenda", "What we cover today") + grid(3, [
        '<div class="pillar"><div class="n">01</div><h3>Variables</h3><ul><li>A name for a value</li><li>Naming rules</li><li>Memory, live</li></ul></div>',
        '<div class="pillar"><div class="n">02</div><h3>The 5 basic types</h3><ul><li>int and float</li><li>str, bool, None</li><li>The float surprise</li></ul></div>',
        '<div class="pillar"><div class="n">03</div><h3>Converting types</h3><ul><li>type(), int(), float(), str()</li><li>Errors you will meet</li><li>Real RetailMart numbers</li></ul></div>',
    ])))
    # 4 story
    S.append(scene("Story: The Price Tag That Was Text", head("Main story", "The price tag that was text",
        "RetailMart product #1 is the Samsung Animi Max, listed at ₹1,25,812.07. A new analyst reads the price from a file and adds ₹100 handling.") +
        grid(3, [
            card("blue", "The setup", '<p>The price comes out of a file looking perfectly normal: <code>125812.07</code>. She stores it in a variable called <code>price</code> and moves on.</p>'),
            card("red", "The bug", '<p>Adding <code>100</code> crashes with a <code>TypeError</code>. So she adds <code>\'100\'</code> instead. No error. The answer is <code>125812.07100</code>: wrong, and silent.</p>'),
            card("green", "The fix", '<p>Files hand Python <b>text</b>. The value was a <code>str</code>, not a number. <code>float()</code> converts it, and now the maths is real maths.</p>'),
        ]) + '<div style="margin-top:20px">' + cell("price = '125812.07'\nprint(price + '100')\nprint(float(price) + 100)") + '</div>'))
    # 5 how it relates to SQL
    S.append(scene("How It Relates to SQL", head("Story → SQL", "Same idea you already know from SQL",
        "In SQL every column has a declared type. In Python the type travels with the value, so you have to stay awake.") +
        '<div class="card"><table class="map"><tr><th>SQL column type</th><th>Python type</th><th>Example</th></tr>'
        '<tr><td>INT / BIGINT</td><td>int</td><td><code>order_id = 1</code></td></tr>'
        '<tr><td>NUMERIC / DOUBLE PRECISION</td><td>float</td><td><code>price = 125812.07</code></td></tr>'
        '<tr><td>TEXT / VARCHAR</td><td>str</td><td><code>product_name = \'Samsung Animi Max\'</code></td></tr>'
        '<tr><td>BOOLEAN</td><td>bool</td><td><code>is_active = True</code></td></tr>'
        '<tr><td>NULL</td><td>None</td><td><code>phone = None</code></td></tr></table></div>'
        + tip("Dates have their own type in both worlds. We meet them in Module 2.")))
    # 6 topic 1 visual: variables
    S.append(scene("A Variable Is a Labelled Box", head("Topic 1 · Variables", "A variable is a name stuck on a value",
        "Write <code>name = value</code>. Python stores the value and remembers the name. Run it and watch the memory table below the cell.") +
        cell("product_name = 'Samsung Animi Max'\nprice = 125812.07\nqty = 2\nin_stock = True\ntotal = price * qty\nprint(total)", vars=True) +
        tip("Change a value and run again. The table always shows what Python remembers right now.")))
    # 7 definition + naming
    S.append(scene("Variables: Syntax and Naming Rules", head("Topic 1 · Variables", "Syntax, rules and a few good habits") + grid(3, [
        card("blue", "Assign", '<p>One <code>=</code> means <b>store</b>, not "equals". The right side is worked out first.</p><p><code>qty = 2 + 3</code></p>'),
        card("green", "Name rules", '<ul><li>letters, digits, underscore</li><li>cannot start with a digit</li><li>no spaces; case matters (<code>Price</code> is not <code>price</code>)</li></ul>'),
        card("purple", "Good habits", '<ul><li><code>snake_case</code> names</li><li>say what it holds: <code>unit_price</code>, not <code>x</code></li><li>one idea per variable</li></ul>'),
    ]) + '<div style="margin-top:20px">' + cell("qty = 2 + 3\nqty = qty + 1   # right side first, then store\nunit_price, tax = 499, 18   # two at once\nprint(qty, unit_price, tax)", vars=True) + '</div>'))
    # 8 mistake: names
    S.append(scene("Mistake: Names and NameError", mistake("Common mistake", "Typo or wrong case in a name",
        "Python does not guess. A name that was never created, or spelled with another case, raises <code>NameError</code>.",
        "price = 125812.07\nprint(Price)", "NameError",
        "price = 125812.07\nprint(price)",
        "Read the last line of the error first: <code>name 'Price' is not defined</code> tells you exactly what Python could not find.")))
    # 9 topic 2: five types
    S.append(scene("The Five Basic Types", head("Topic 2 · Types", "Five types cover most of an analyst's day",
        "<code>type()</code> tells you what a value is. Try each one.") +
        grid(5, [
            card("blue", "int", '<p>whole numbers: IDs, counts</p><p><code>order_id = 1</code></p>'),
            card("green", "float", '<p>decimals: prices, ratios</p><p><code>price = 125812.07</code></p>'),
            card("orange", "str", '<p>text in quotes</p><p><code>city = \'Gwalior\'</code></p>'),
            card("purple", "bool", '<p>True or False</p><p><code>is_active = True</code></p>'),
            card("red", "None", '<p>"no value", like NULL</p><p><code>phone = None</code></p>'),
        ]) + '<div style="margin-top:20px">' + cell("print(type(1), type(125812.07), type('Gwalior'), type(True), type(None))\nprint(type('1'), type(1))   # same look, different type") + '</div>'))
    # 10 definition: where each is used
    S.append(scene("int, float, str, bool, None in RetailMart", head("Topic 2 · Types", "Which type fits which RetailMart column") +
        '<div class="card"><table class="map"><tr><th>Column</th><th>Python type</th><th>Why</th></tr>'
        '<tr><td>orders.order_id</td><td>int</td><td>whole number, never 2.5 orders</td></tr>'
        '<tr><td>orders.net_total</td><td>float</td><td>rupees and paise</td></tr>'
        '<tr><td>stores.city</td><td>str</td><td>text, in quotes</td></tr>'
        '<tr><td>a yes/no flag</td><td>bool</td><td>exactly True or False</td></tr>'
        '<tr><td>missing phone</td><td>None</td><td>unknown, not zero and not empty text</td></tr></table></div>'
        '<div style="margin-top:20px">' + cell("order_id = 1\nnet_total = 22033.22\ncity = 'Gwalior'\nphone = None\nprint(order_id, net_total, city, phone)\nprint(phone is None)", vars=True) + '</div>'
        + tip("Test for missing with <code>is None</code>, never <code>== None</code>.")))
    # 11 float surprise
    S.append(scene("The Float Surprise", mistake("Common mistake", "0.1 + 0.2 is not exactly 0.3",
        "Computers store decimals in binary, so some come out a tiny bit off. It even happens with real RetailMart prices.",
        "price = 125812.07\ncost = 88068.45\nprint(price - cost)\nprint(0.1 + 0.2 == 0.3)", None,
        "price = 125812.07\ncost = 88068.45\nprint(round(price - cost, 2))\nprint(round(0.1 + 0.2, 2) == 0.3)",
        "Round for display and comparison. For exact money in finance code, use <code>Decimal</code>; we meet it in the numbers topic.")))
    # 12 conversion
    S.append(scene("Converting Between Types", head("Topic 3 · Converting", "int(), float(), str(), bool() change the type",
        "Data from files and websites arrives as text. Convert it before you do maths.") + grid(2, [
            cell("print(int('42') + 1)\nprint(float('125812.07') + 100)\nprint(str(499) + ' rupees')\nprint(type(float('3.5')))"),
            cell("print(int(3.99))      # cuts, does not round\nprint(round(3.99))    # rounds\nprint(bool(0), bool(''), bool(None))\nprint(bool(1), bool('False'))"),
        ]) + warn("<code>bool('False')</code> is <b>True</b>. Any non-empty text is True. Only <code>0</code>, empty text, <code>None</code> and empty collections are False.")))
    # 13 mistake: conversion errors
    S.append(scene("Mistake: Conversion Errors", mistake("Common mistake", "int() on text that is not a plain number",
        "<code>int()</code> only accepts digits. Decimals and Indian-style commas raise <code>ValueError</code>.",
        "print(int('1,25,812'))", "ValueError",
        "text = '1,25,812'\nprint(int(text.replace(',', '')))\nprint(int(float('12.5')))",
        "Clean first (<code>replace</code>), then convert. For '12.5' go through <code>float()</code> first.")))
    # 14 mistake: str + int
    S.append(scene("Mistake: TypeError", mistake("Common mistake", "Adding text and a number",
        "Python is strict: it will not mix <code>str</code> and <code>int</code> with <code>+</code>.",
        "price = '125812'\nprint(price + 100)", "TypeError",
        "price = '125812'\nprint(int(price) + 100)",
        "<code>can only concatenate str (not \"int\") to str</code> means one side is still text. Convert it.")))
    # 15 real world
    S.append(scene("Real World: Margin on a RetailMart Product", head("Real world", "Margin on RetailMart product #1",
        "Samsung Animi Max: price ₹1,25,812.07, cost ₹88,068.45. Variables make the formula readable.") +
        cell("price = 125812.07\ncost = 88068.45\nmargin = round(price - cost, 2)\nmargin_pct = round(margin / price * 100, 2)\nprint('Margin in rupees:', margin)\nprint('Margin percent:', margin_pct)", vars=True)
        + tip("This is what a SQL <code>SELECT price - cost AS margin</code> does for every row. In Module 2 pandas does it for all 6,036 products at once.")))
    # 16-17 practice
    P1 = [
        practice("Easy", "Store the price 125812.07 in a variable called <code>price</code> and print it.", "price = \nprint(price)", "125812.07", "price = 125812.07\nprint(price)"),
        practice("Easy", "Print the type of the value <code>'125812'</code> (with quotes).", "print()", "<class 'str'>", "print(type('125812'))"),
        practice("Medium", "<code>price</code> arrives as text. Print the total for <code>qty = 3</code> as a number.", "price = '125812'\nqty = 3\nprint()", "377436", "price = '125812'\nqty = 3\nprint(int(price) * qty)"),
        practice("Medium", "Print the margin (price minus cost) rounded to 2 decimals.", "price = 125812.07\ncost = 88068.45\nprint()", "37743.62", "price = 125812.07\ncost = 88068.45\nprint(round(price - cost, 2))"),
    ]
    P2 = [
        practice("Hard", "Turn <code>'1,25,812'</code> into a number and add 1000.", "text = '1,25,812'\nprint()", "126812", "text = '1,25,812'\nprint(int(text.replace(',', '')) + 1000)"),
        practice("Hard", "Predict first, then print <code>bool(''), bool('False'), bool(0)</code> separated by spaces.", "print()", "False True False", "print(bool(''), bool('False'), bool(0))"),
        practice("Crazy", "Swap <code>a</code> and <code>b</code> in ONE line (no third variable), then print them.", "a = 1\nb = 2\n\nprint(a, b)", "2 1", "a = 1\nb = 2\na, b = b, a\nprint(a, b)"),
        practice("Crazy", "<code>y = x</code> then <code>x</code> changes. Print what <code>y</code> is now.", "x = 10\ny = x\nx = 20\nprint()", "10", "x = 10\ny = x\nx = 20\nprint(y)"),
    ]
    S.append(scene("Practice Arena: Easy and Medium", head("Practice Arena", "Easy and Medium", "Type the answer, press Run. Green means correct.") + grid(2, P1)))
    S.append(scene("Practice Arena: Hard and Crazy", head("Practice Arena", "Hard and Crazy", "Predict before you run. These are the traps interviewers like.") + grid(2, P2)))
    # 18 interview
    S.append(scene("Interview Studio", head("Interview Studio", "Five questions interviewers ask on day one") + grid(2, [
        reveal("What is the difference between int and float?", "<code>int</code> holds whole numbers, <code>float</code> holds decimals. <code>5</code> is an int, <code>5.0</code> is a float, and they compare equal (<code>5 == 5.0</code> is True)."),
        reveal("Why is 0.1 + 0.2 not exactly 0.3?", "Floats are stored in binary and 0.1 has no exact binary form. The result is <code>0.30000000000000004</code>. Round for display, or use <code>Decimal</code> for exact money."),
        reveal("Is Python statically or dynamically typed?", "Dynamically typed (a name can point to any type) and strongly typed (<code>'1' + 1</code> is an error, it does not guess)."),
        reveal("What is None, and how do you test for it?", "<code>None</code> is the single 'no value' object, Python's NULL. Test with <code>x is None</code>."),
        reveal("What does bool('False') return?", "<code>True</code>. Any non-empty string is truthy, whatever it says."),
    ])))
    # 19 self check
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these without running code?", "Click a card to check yourself.") + grid(3, [
        reveal("What does <code>type('7')</code> show?", "<code>&lt;class 'str'&gt;</code>. Quotes make it text."),
        reveal("What happens with <code>'5' + 5</code>?", "<code>TypeError</code>. Convert one side."),
        reveal("<code>int(3.99)</code> gives?", "<code>3</code>. It cuts the decimals; it does not round."),
        reveal("Is <code>Price</code> the same as <code>price</code>?", "No. Names are case-sensitive."),
        reveal("How do you check a value is missing?", "<code>value is None</code>"),
        reveal("<code>a, b = b, a</code> does what?", "Swaps the two values in one line."),
    ])))
    # 20 takeaways
    S.append(scene("Key Takeaways", head("Key Takeaways", "Five rules to remember") + grid(3, [
        card("blue", "1 · A variable is a name", '<p><code>name = value</code> stores; the right side is worked out first.</p>'),
        card("green", "2 · Five types", '<p><code>int, float, str, bool, None</code>. Ask <code>type()</code> when unsure.</p>'),
        card("orange", "3 · Files give text", '<p>Convert with <code>int()</code>, <code>float()</code>, <code>str()</code> before maths.</p>'),
        card("red", "4 · Floats drift", '<p>Round for display. Exact money needs <code>Decimal</code>.</p>'),
        card("purple", "5 · None is missing", '<p>Test with <code>is None</code>. Not zero, not empty text.</p>'),
        card("blue", "6 · Read the last error line", '<p><code>NameError</code>, <code>TypeError</code>, <code>ValueError</code> each say what is wrong.</p>'),
    ])))
    # 21 quick reference
    def qr(t, code): return f'<div><h3>{t}</h3>{cell(code)}</div>'
    S.append(scene("Quick Reference", head("Quick Reference", "Every syntax from today") + grid(3, [
        qr("Assign", "price = 125812.07\nqty, tax = 2, 18\nprint(price, qty, tax)"),
        qr("Check a type", "price = 125812.07\nprint(type(price))"),
        qr("Convert", "print(int('42'), float('1.5'), str(7), bool(1))"),
        qr("Round", "print(round(37743.62000000001, 2))"),
        qr("Missing value", "phone = None\nprint(phone is None)"),
        qr("Swap", "a, b = 1, 2\na, b = b, a\nprint(a, b)"),
    ])))
    # 22 take-home
    S.append(scene("Take-Home Challenge", head("Take-Home Challenge", "Product #2 of RetailMart",
        "Samsung Recusandae Lite: price ₹1,06,495.49, cost ₹74,546.84. Work in the cell below, then check against a classmate or in a 1:1.") + grid(2, [
        '<div class="card"><ol style="padding-left:20px;color:var(--muted);line-height:1.9"><li>Store price, cost and the product name in variables.</li><li>Print the margin in rupees, rounded to 2 decimals.</li><li>Print the margin percent, rounded to 2 decimals.</li><li>The price arrives as <code>\'1,06,495.49\'</code>. Convert it to a float.</li><li>Print <code>type()</code> of every variable you made.</li></ol></div>',
        cell("# your work here\nname = 'Samsung Recusandae Lite'\n", vars=True, rows=9),
    ])))
    # 23 journey
    import curriculum_data
    topics = [t["title"] for t in curriculum_data.MODULES[1]["topics"] if t["n"].isdigit()]
    j = "".join(f'<span class="{"here" if i == 1 else ("done" if i < 1 else "")}">{i+1}. {t}</span>' for i, t in enumerate(topics))
    S.append(scene("Your Python Journey", head("Your Python journey", "Module 1: Python Foundations", "You are here: topic 2 of 29.") + f'<div class="journey">{j}</div>'))
    # 24 next
    S.append(scene("Next: Numbers & Operators", head("Next topic", "Numbers & Operators",
        "Arithmetic, integer division, modulo, powers, rounding, and exact money with <code>Decimal</code>. You will use every one of them on RetailMart orders.") +
        '<div class="mission"><b>Before the next topic:</b> finish the take-home and play with the playground: <a href="/playground/">python.theshiraverse.com/playground</a></div>'))
    return S
