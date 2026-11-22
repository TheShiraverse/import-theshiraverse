from deck_lib import *

META = dict(
    module=1, num=3, slug="numbers-operators", title="Numbers & Operators",
    desc="Python Module 1, topic 3: arithmetic with + - * / // % **, operator precedence, rounding, the math module, and exact money with Decimal. Run every example in your browser.",
    mission="do arithmetic correctly: split amounts, add GST, round the Python way, and keep money exact.",
    next=("Strings 1: Text Basics", "strings-text-basics"),
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(scene("Today's Agenda", head("Agenda", "What we cover today") + grid(3, [
        '<div class="pillar"><div class="n">01</div><h3>The operators</h3><ul><li>+ - * and /</li><li>// and % for splitting</li><li>** and precedence</li></ul></div>',
        '<div class="pillar"><div class="n">02</div><h3>Built-ins and math</h3><ul><li>abs, round, divmod, min, max</li><li>The math module</li><li>Rounding the Python way</li></ul></div>',
        '<div class="pillar"><div class="n">03</div><h3>Exact money</h3><ul><li>Why floats drift</li><li>Decimal and Fraction</li><li>A real GST invoice</li></ul></div>',
    ])))
    S.append(scene("Story: The Rupee That Vanished", head("Main story", "The rupee that vanished",
        "Three friends split a ₹1,000 RetailMart bill. The analyst's script says everyone pays ₹333. The shop is left ₹1 short.") +
        grid(3, [
            card("blue", "The setup", '<p>Bill: ₹1,000. People: 3. She writes <code>1000 // 3</code> because she wants whole rupees.</p>'),
            card("red", "The bug", '<p><code>3 × 333 = 999</code>. One rupee is simply gone, and no error is shown.</p>'),
            card("green", "The fix", '<p><code>//</code> gives the share, <code>%</code> gives what is left over. <code>divmod()</code> gives both at once.</p>'),
        ]) + '<div style="margin-top:20px">' + cell("bill, people = 1000, 3\nprint(bill // people)\nprint(bill % people)\nprint(divmod(bill, people))") + '</div>'))
    S.append(scene("How It Relates to SQL", head("Story → SQL", "Same maths, a few different surprises",
        "You already used these in PostgreSQL. Python mostly agrees, but three things differ.") +
        table(["Idea", "PostgreSQL", "Python", "Careful"], [
            ["Divide", "<code>7 / 2</code> = 3", "<code>7 / 2</code> = 3.5", "Python <code>/</code> never drops decimals"],
            ["Whole-number divide", "<code>7 / 2</code> (ints)", "<code>7 // 2</code> = 3", "Python needs <code>//</code>"],
            ["Remainder", "<code>MOD(7, 2)</code>", "<code>7 % 2</code> = 1", "Same idea"],
            ["Power", "<code>POWER(2, 3)</code> or <code>2 ^ 3</code>", "<code>2 ** 3</code> = 8", "Python <code>^</code> is XOR, not power"],
            ["Round", "<code>ROUND(2.5)</code> = 3", "<code>round(2.5)</code> = 2", "Python rounds .5 to the even number"],
            ["Biggest / smallest", "<code>GREATEST / LEAST</code>", "<code>max() / min()</code>", "Python takes a list or several values"],
        ]) + tip("Rule of thumb: when SQL and Python give different answers, Python is usually the one doing exactly what its own rules say.")))
    S.append(scene("Topic 1: The Basic Operators", head("Topic 1 · Operators", "Add, subtract, multiply, divide",
        "<code>+  -  *  /</code> work as you expect. Note that <code>/</code> always gives a <code>float</code>, even when the answer is whole.") +
        cell("price = 499\nqty = 3\nprint(price * qty)\nprint(price + 100)\nprint(price - 99)\nprint(price / qty)\nprint(10 / 2)   # still a float", vars=True) +
        tip("Mixing an int and a float gives a float: <code>2 + 0.5</code> is <code>2.5</code>.")))
    S.append(scene("Topic 1: // and % for Splitting", head("Topic 1 · Operators", "Whole-number divide and remainder",
        "<code>//</code> is floor division: it drops the decimals. <code>%</code> (modulo) is what is left over. Together they split things into groups.") + grid(2, [
            cell("print(17 // 5)   # whole groups\nprint(17 % 5)    # leftover\nprint(divmod(17, 5))\nprint(5 * 3 + 2)"),
            cell("# is it even?\nprint(10 % 2 == 0)\nprint(7 % 2 == 0)\n# minutes to hours and minutes\nprint(divmod(135, 60))"),
        ]) + tip("<code>x % 2 == 0</code> is the classic even check. <code>x % 7</code> is how you find the day of the week in a cycle.")))
    S.append(scene("Topic 1: Powers and Roots", head("Topic 1 · Operators", "** is power",
        "<code>**</code> raises to a power. A fractional power is a root. This is how compound interest works.") + grid(2, [
            cell("print(2 ** 3)\nprint(2 ** 10)\nprint(9 ** 0.5)    # square root\nprint(10 ** -2)"),
            cell("# ₹10,000 at 8% a year for 3 years\nprint(round(10000 * 1.08 ** 3, 2))"),
        ]) + tip("Python integers never overflow: <code>2 ** 100</code> just works.")))
    S.append(scene("Topic 2: Operator Precedence", head("Topic 2 · Precedence", "Who goes first? Brackets decide",
        "Python follows the maths order: brackets, then <code>**</code>, then <code>* / // %</code>, then <code>+ -</code>. When unsure, add brackets.") + grid(2, [
            cell("print(2 + 3 * 4)\nprint((2 + 3) * 4)\nprint(100 - 20 - 5)\nprint(2 ** 3 ** 2)   # right to left"),
            cell("print(-2 ** 2)     # power first, then minus\nprint((-2) ** 2)\nprint(10 + 5 * 2 // 3)"),
        ]) + warn("<code>-2 ** 2</code> is <b>-4</b>, not 4. The power happens before the minus sign.")))
    S.append(scene("Augmented Assignment", head("Topic 2 · Shortcuts", "+= and friends update a variable in place",
        "<code>x += 5</code> means <code>x = x + 5</code>. Every operator has one: <code>-=  *=  /=  //=  %=  **=</code>.") +
        cell("total = 0\ntotal += 499\ntotal += 250\ntotal *= 2      # double it\ntotal -= 100\nprint(total)\n\ncount = 17\ncount //= 5\nprint(count)", vars=True)))
    S.append(scene("Mistake: ZeroDivisionError", mistake("Common mistake", "Dividing by zero",
        "Maths says undefined, so Python stops with <code>ZeroDivisionError</code>. It happens on <code>/</code>, <code>//</code> and <code>%</code>.",
        "revenue = 5000\norders = 0\nprint(revenue / orders)", "ZeroDivisionError",
        "revenue = 5000\norders = 0\nif orders == 0:\n    print('no orders, no average')\nelse:\n    print(revenue / orders)",
        "Check the divisor before you divide. An empty day in RetailMart has zero orders, and an average of nothing is not a number.")))
    S.append(scene("Mistake: Floor Division and Negatives", mistake("Common mistake", "-7 // 2 is -4, not -3",
        "<code>//</code> rounds <b>down</b> (towards minus infinity), not towards zero. The remainder follows the same rule.",
        "print(-7 // 2)\nprint(-7 % 2)\nprint(int(-7 / 2))", None,
        "import math\nprint(math.trunc(-7 / 2))\nprint(-7 // 2)\nprint(divmod(-7, 2))",
        "Rule: <code>a == (a // b) * b + a % b</code> always holds. If you want to cut towards zero, use <code>int()</code> or <code>math.trunc()</code>.")))
    S.append(scene("Mistake: ^ Is Not Power", mistake("Common mistake", "2 ^ 3 is not 8",
        "In PostgreSQL <code>^</code> is power. In Python it is <b>XOR</b> (a bitwise operator), and it runs without any error.",
        "print(2 ^ 3)\nprint(10 ^ 2)", None,
        "print(2 ** 3)\nprint(10 ** 2)",
        "No error means no warning. If a power result looks small and strange, check you wrote <code>**</code>.")))
    S.append(scene("Topic 3: Number Built-ins", head("Topic 3 · Built-ins", "abs, round, divmod, min, max, sum, pow",
        "Python ships with small helpers for everyday number work. No import needed.") + grid(2, [
            cell("print(abs(-250))\nprint(round(3.14159, 2))\nprint(divmod(1000, 3))\nprint(pow(2, 10))"),
            cell("print(min(499, 250, 899))\nprint(max(499, 250, 899))\nprint(sum([499, 250, 899]))\nprint(max(3, 7.5))"),
        ]) + tip("<code>round(x)</code> with no second argument gives an <b>int</b>. <code>round(x, 2)</code> keeps two decimals and stays a float.")))
    S.append(scene("Mistake: round() and Half to Even", mistake("Common mistake", "round(2.5) is 2",
        "Python uses <b>banker's rounding</b>: a value exactly halfway goes to the nearest <b>even</b> number. It avoids always rounding up, but it surprises everyone.",
        "print(round(0.5), round(1.5), round(2.5), round(3.5))\nprint(round(2.675, 2))", None,
        "from decimal import Decimal, ROUND_HALF_UP\nprint(Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP))\nprint(Decimal('2.675').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))",
        "For rounding that matches a printed bill (half up), use <code>Decimal</code> with <code>ROUND_HALF_UP</code>. <code>round(2.675, 2)</code> gives 2.67 because the float is stored a hair below 2.675.")))
    S.append(scene("Topic 3: The math Module", head("Topic 3 · math", "import math for the rest",
        "A module is a toolbox you bring in with <code>import</code>. <code>math</code> comes with Python.") + grid(2, [
            cell("import math\nprint(math.sqrt(144))\nprint(math.pi)\nprint(math.ceil(4.1))\nprint(math.floor(4.9))\nprint(math.trunc(-4.9))"),
            cell("import math\nprint(math.log10(1000))\nprint(math.factorial(5))\nprint(math.isclose(0.1 + 0.2, 0.3))\nprint(0.1 + 0.2 == 0.3)"),
        ]) + tip("Use <code>math.isclose()</code> to compare floats. Never trust <code>==</code> on decimals that came from arithmetic.")))
    S.append(scene("Topic 4: float, Decimal, Fraction", head("Topic 4 · Exact numbers", "Three ways to hold a decimal",
        "A <code>float</code> is fast but tiny errors creep in. <code>Decimal</code> is exact for money. <code>Fraction</code> is exact for ratios.") + grid(3, [
            card("red", "float", '<p>Fast, approximate. Fine for statistics and measurements.</p>' + cell("print(0.1 + 0.2)\nprint(1.1 * 3)", rows=2)),
            card("green", "Decimal", '<p>Exact decimal digits. Use for rupees and paise.</p>' + cell("from decimal import Decimal\nprint(Decimal('0.1') + Decimal('0.2'))\nprint(Decimal('1.10') * 3)", rows=3)),
            card("blue", "Fraction", '<p>Exact ratios as a / b.</p>' + cell("from fractions import Fraction\nprint(Fraction(1, 3) * 3)\nprint(Fraction(1, 3) + Fraction(1, 6))", rows=3)),
        ])))
    S.append(scene("Mistake: Decimal Traps", mistake("Common mistake", "Decimal from a float, or Decimal plus float",
        "<code>Decimal(0.1)</code> copies the float's error. And a <code>Decimal</code> will not mix with a <code>float</code>.",
        "from decimal import Decimal\nprint(Decimal(0.1))\nprint(Decimal('10.50') + 0.25)", "TypeError",
        "from decimal import Decimal\nprint(Decimal('0.1'))\nprint(Decimal('10.50') + Decimal('0.25'))",
        "Always build a <code>Decimal</code> from <b>text</b> (<code>Decimal('0.1')</code>), and keep every number in the sum a <code>Decimal</code>.")))
    S.append(scene("Literals: Underscores, Complex, Bitwise", head("Topic 5 · Odds and ends", "Three small things worth knowing",
        "You will not use these daily, but you will meet them in other people's code.") + grid(3, [
            card("blue", "Underscores", '<p>Readable big numbers. Python ignores the <code>_</code>, so Indian grouping works.</p>' + cell("print(1_25_812)\nprint(1_000_000 == 10_00_000)", rows=2)),
            card("purple", "Complex", '<p>Engineering and signal maths. Rare in data work.</p>' + cell("z = 3 + 4j\nprint(abs(z))\nprint(z.real, z.imag)", rows=3)),
            card("orange", "Bitwise", '<p><code>&amp; | ^ ~ &lt;&lt; &gt;&gt;</code> work on binary digits. Mostly flags and low-level code.</p>' + cell("print(6 & 3, 6 | 3, 6 ^ 3)\nprint(1 << 4)", rows=2)),
        ])))
    S.append(scene("Real World: GST Invoice", head("Real world", "A GST invoice for RetailMart product #1",
        "Samsung Animi Max, ₹1,25,812.07, quantity 2, GST 18%. Money uses <code>Decimal</code> so the paise are exact.") +
        cell("from decimal import Decimal, ROUND_HALF_UP\n\nprice = Decimal('125812.07')\nqty = 2\nsubtotal = price * qty\ngst = (subtotal * Decimal('0.18')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)\ntotal = subtotal + gst\n\nprint('Subtotal:', subtotal)\nprint('GST 18%:', gst)\nprint('Total   :', total)", vars=True, rows=12) +
        tip("A shop prints the rounded GST on the bill, so the code must round the same way. That is why we use <code>quantize</code> and not <code>round()</code>.")))
    S.append(scene("Real World: Change-Making", head("Real world", "Change for a ₹2,860 refund",
        "The cashier has notes of ₹500, ₹100, ₹50 and ₹10. <code>divmod()</code> hands out the biggest note first and passes the rest down.") +
        cell("amount = 2860\nn500, amount = divmod(amount, 500)\nn100, amount = divmod(amount, 100)\nn50, amount = divmod(amount, 50)\nn10, amount = divmod(amount, 10)\nprint('500s:', n500, '100s:', n100, '50s:', n50, '10s:', n10, 'left:', amount)", vars=True, rows=7) +
        tip("In topic 13 a loop does this for any list of notes. Today you can already see the idea.")))
    P1 = [
        practice("Easy", "Print the whole-number quotient and the remainder of 17 divided by 5, on one line.", "print()", "3 2", "print(17 // 5, 17 % 5)"),
        practice("Easy", "A customer buys 3 items at ₹499 and 2 items at ₹250. Print the total.", "print()", "1997", "print(3 * 499 + 2 * 250)"),
        practice("Medium", "Add 18% GST to ₹1,000 using brackets. Print the result rounded to 2 decimals.", "print()", "1180.0", "print(round(1000 * (1 + 18 / 100), 2))"),
        practice("Medium", "Split ₹1,000 among 3 people. Print the share and the leftover rupee together using <code>divmod</code>.", "print()", "(333, 1)", "print(divmod(1000, 3))"),
    ]
    P2 = [
        practice("Hard", "Predict first, then print <code>-7 // 2</code> and <code>-7 % 2</code> on one line.", "print()", "-4 1", "print(-7 // 2, -7 % 2)"),
        practice("Hard", "Print <code>round(2.5)</code>, <code>round(3.5)</code> and <code>round(0.5)</code> on one line.", "print()", "2 4 0", "print(round(2.5), round(3.5), round(0.5))"),
        practice("Crazy", "Print the exact sum of 0.1 and 0.2 so it shows <code>0.3</code>. Use <code>Decimal</code>.", "from decimal import Decimal\nprint()", "0.3", "from decimal import Decimal\nprint(Decimal('0.1') + Decimal('0.2'))"),
        practice("Crazy", "475 minutes is how many hours and minutes? Print them as <code>7 55</code> style using one <code>divmod</code>.", "h, m = \nprint(h, m)", "7 55", "h, m = divmod(475, 60)\nprint(h, m)"),
    ]
    S.append(scene("Practice Arena: Easy and Medium", head("Practice Arena", "Easy and Medium", "Type the answer, press Run. Green means correct.") + grid(2, P1)))
    S.append(scene("Practice Arena: Hard and Crazy", head("Practice Arena", "Hard and Crazy", "Predict before you run. These are the traps interviewers like.") + grid(2, P2)))
    S.append(scene("Interview Studio", head("Interview Studio", "Five questions interviewers ask about numbers") + grid(2, [
        reveal("What is the difference between / and //?", "<code>/</code> is true division and always returns a float (<code>7 / 2</code> is <code>3.5</code>). <code>//</code> is floor division and rounds down (<code>7 // 2</code> is <code>3</code>, and <code>-7 // 2</code> is <code>-4</code>)."),
        reveal("What does round(2.5) return, and why?", "<code>2</code>. Python uses banker's rounding: exact halves go to the nearest even number. <code>round(3.5)</code> is <code>4</code>."),
        reveal("Why not use float for money?", "Floats are binary, so values like 0.1 are slightly off and errors add up. Use <code>Decimal</code> built from text, or keep whole paise as integers."),
        reveal("What does 2 ^ 3 give in Python?", "<code>1</code>. <code>^</code> is bitwise XOR. Power is <code>**</code>, so <code>2 ** 3</code> is <code>8</code>."),
        reveal("Does Python have an integer overflow?", "No. Integers grow as needed, so <code>2 ** 100</code> is <code>1267650600228229401496703205376</code>. Floats do have limits."),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these without running code?", "Click a card to check yourself.") + grid(3, [
        reveal("<code>7 / 2</code> and <code>7 // 2</code>?", "<code>3.5</code> and <code>3</code>."),
        reveal("<code>2 + 3 * 4</code>?", "<code>14</code>. Multiply first."),
        reveal("<code>2 ** 3 ** 2</code>?", "<code>512</code>. Powers go right to left: <code>3 ** 2 = 9</code>, then <code>2 ** 9</code>."),
        reveal("<code>-2 ** 2</code>?", "<code>-4</code>. Power first, then the minus."),
        reveal("<code>10 % 3</code>?", "<code>1</code>. 3 fits three times (9), 1 is left."),
        reveal("<code>round(2.5)</code>?", "<code>2</code>. Half goes to the even number."),
    ])))
    S.append(scene("Key Takeaways", head("Key Takeaways", "Six rules to remember") + grid(3, [
        card("blue", "1 · / is always a float", '<p><code>//</code> floors, <code>%</code> is the leftover, <code>divmod()</code> gives both.</p>'),
        card("green", "2 · ** is power", '<p><code>^</code> is XOR. A fractional power is a root.</p>'),
        card("orange", "3 · Brackets win", '<p>When unsure, add brackets. <code>-2 ** 2</code> is <code>-4</code>.</p>'),
        card("red", "4 · round() is half to even", '<p><code>round(2.5)</code> is <code>2</code>. Use <code>Decimal</code> for bill-style rounding.</p>'),
        card("purple", "5 · Money is Decimal", '<p>Build it from text, never mix with float, round with <code>quantize</code>.</p>'),
        card("blue", "6 · Check the divisor", '<p>Dividing by zero raises <code>ZeroDivisionError</code>. Test first.</p>'),
    ])))
    def qr(t, code): return f'<div><h3>{t}</h3>{cell(code)}</div>'
    S.append(scene("Quick Reference", head("Quick Reference", "Every syntax from today") + grid(3, [
        qr("Operators", "print(7 + 2, 7 - 2, 7 * 2, 7 / 2)\nprint(7 // 2, 7 % 2, 7 ** 2)"),
        qr("Split", "print(divmod(1000, 3))"),
        qr("Update in place", "total = 100\ntotal += 50\ntotal *= 2\nprint(total)"),
        qr("Built-ins", "print(abs(-5), round(3.14159, 2), min(4, 9), max(4, 9), sum([1, 2, 3]))"),
        qr("math", "import math\nprint(math.sqrt(81), math.ceil(2.1), math.floor(2.9))"),
        qr("Exact money", "from decimal import Decimal\nprint(Decimal('0.10') + Decimal('0.20'))"),
    ])))
    S.append(scene("Take-Home Challenge", head("Take-Home Challenge", "Invoice for product #2 of RetailMart",
        "Samsung Recusandae Lite: price ₹1,06,495.49, quantity 3, GST 18%. Work in the cell below, then check against a classmate or in a 1:1.") + grid(2, [
        '<div class="card"><ol style="padding-left:20px;color:var(--muted);line-height:1.9"><li>Store the price as a <code>Decimal</code> (from text).</li><li>Compute the subtotal for 3 units.</li><li>Compute GST at 18%, rounded half up to 2 decimals.</li><li>Print the total.</li><li>Split the total among 4 friends with <code>divmod</code> on whole rupees. Print share and leftover.</li></ol></div>',
        cell("# your work here\nfrom decimal import Decimal, ROUND_HALF_UP\nprice = Decimal('106495.49')\n", vars=True, rows=10),
    ])))
    import curriculum_data
    topics = [t["title"] for t in curriculum_data.MODULES[1]["topics"] if t["n"].isdigit()]
    j = "".join(f'<span class="{"here" if i == 2 else ("done" if i < 2 else "")}">{i+1}. {t}</span>' for i, t in enumerate(topics))
    S.append(scene("Your Python Journey", head("Your Python journey", "Module 1: Python Foundations", "You are here: topic 3 of 29.") + f'<div class="journey">{j}</div>'))
    S.append(scene("Next: Strings 1: Text Basics", head("Next topic", "Strings 1: Text Basics",
        "Slice, index and inspect text: card numbers, names, file extensions. Everything RetailMart stores as a word.") +
        '<div class="mission"><b>Before the next topic:</b> finish the take-home and try it in the playground: <a href="/playground/">python.theshiraverse.com/playground</a></div>'
        '<div style="margin-top:20px"><a class="btn-next" href="/notes/module-1/strings-text-basics/">Next: Strings 1: Text Basics &rarr;</a></div>'))
    return S
