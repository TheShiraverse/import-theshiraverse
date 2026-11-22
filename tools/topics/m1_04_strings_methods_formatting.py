from deck_lib import *

META = dict(
    module=1, num=5, slug="strings-methods-formatting", title="Strings 2: Methods & Formatting",
    desc="Python Module 1, topic 5: clean text with upper, strip, split, join and replace, search with find and count, and format output with f-strings. Run every example in your browser.",
    mission="clean messy text and print it neatly: tidy names, split a line of data and format an invoice.",
    next=("Booleans, Comparison & Logic", "booleans-comparison-logic"),
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(scene("Today's Agenda", head("Agenda", "What we cover today") + grid(3, [
        '<div class="pillar"><div class="n">01</div><h3>Clean text</h3><ul><li>upper, lower, title</li><li>strip</li><li>replace</li></ul></div>',
        '<div class="pillar"><div class="n">02</div><h3>Cut and search</h3><ul><li>split and join</li><li>find, index, count</li><li>startswith, isdigit</li></ul></div>',
        '<div class="pillar"><div class="n">03</div><h3>Format output</h3><ul><li>f-strings</li><li>Width, decimals, thousands</li><li>format() and %</li></ul></div>',
    ])))
    S.append(scene("Story: Three Gwaliors", head("Main story", "Three Gwaliors",
        "A RetailMart city report counts customers per city. It shows Gwalior three times, each with a small count. Nothing is wrong with the data except how the cities were typed.") +
        grid(3, [
            card("red", "The problem", '<p>People typed <code>gwalior</code>, <code> Gwalior </code> and <code>GWALIOR</code>. To a computer these are three different texts.</p>'),
            card("blue", "The idea", '<p>Clean first, count after. <code>strip()</code> removes stray spaces and <code>title()</code> fixes the capitals.</p>'),
            card("green", "The result", '<p>One clean name, so one correct total.</p>'),
        ]) + '<div style="margin-top:20px">' + cell("raw = ['gwalior', ' Gwalior ', 'GWALIOR']\nprint(len(set(raw)))\nclean = [c.strip().title() for c in raw]\nprint(clean)\nprint(len(set(clean)))") + '</div>'))
    S.append(scene("How It Relates to SQL", head("Story → SQL", "The text functions you know, as methods",
        "In SQL you wrap a column in a function. In Python you call a <b>method</b> with a dot after the text.") +
        table(["Job", "PostgreSQL", "Python"], [
            ["Upper / lower", "<code>UPPER(s)</code>, <code>LOWER(s)</code>", "<code>s.upper()</code>, <code>s.lower()</code>"],
            ["Trim spaces", "<code>TRIM(s)</code>", "<code>s.strip()</code>"],
            ["Replace", "<code>REPLACE(s, 'a', 'b')</code>", "<code>s.replace('a', 'b')</code>"],
            ["Split", "<code>SPLIT_PART(s, ',', 2)</code> (starts at 1)", "<code>s.split(',')[1]</code> (starts at 0)"],
            ["Format a number", "<code>TO_CHAR(n, 'FM999,999.00')</code>", "<code>f'{n:,.2f}'</code>"],
        ]) + tip("Methods are written <code>text.method()</code>. They do not change the text: they hand back a new one.")))
    S.append(scene("Topic 1: Case Methods", head("Topic 1 · Clean text", "upper, lower, title, capitalize",
        "Case methods fix inconsistent capitals. Always compare after making the case the same.") + grid(2, [
            cell("s = 'samsung animi MAX'\nprint(s.upper())\nprint(s.lower())\nprint(s.title())\nprint(s.capitalize())"),
            cell("a = 'GWALIOR'\nb = 'gwalior'\nprint(a == b)\nprint(a.lower() == b.lower())"),
        ])))
    S.append(scene("Topic 1: strip and replace", head("Topic 1 · Clean text", "Remove spaces, swap pieces",
        "<code>strip()</code> trims both ends (also <code>lstrip</code> and <code>rstrip</code>). <code>replace(old, new)</code> swaps every match.") + grid(2, [
            cell("s = '  Gwalior \\n'\nprint(repr(s))\nprint(repr(s.strip()))\nprint(repr(s.lstrip()))\nprint(repr(s.rstrip()))"),
            cell("price = '1,25,812.07'\nprint(price.replace(',', ''))\nprint(float(price.replace(',', '')))\nprint('a-b-c'.replace('-', '/', 1))"),
        ]) + tip("<code>repr()</code> shows hidden spaces and newlines, so use it when text looks right but behaves wrong.")))
    S.append(scene("Topic 2: split and join", head("Topic 2 · Cut and glue", "split cuts text into a list, join glues it back",
        "<code>split(sep)</code> returns a list of pieces. <code>sep.join(list)</code> puts them together with <code>sep</code> between.") + grid(2, [
            cell("line = 'Priya,Gwalior,499'\nparts = line.split(',')\nprint(parts)\nprint(parts[1])\nname, city, amount = parts\nprint(city)", vars=True),
            cell("words = ['Samsung', 'Animi', 'Max']\nprint(' '.join(words))\nprint('-'.join(words))\nprint(''.join(words))\nprint('22-11-2026'.split('-'))"),
        ]) + tip("Splitting on <code>','</code> is how you read one row of a CSV file. Topic 24 covers the real thing.")))
    S.append(scene("Topic 2: find, index, count", head("Topic 2 · Search", "Where is it, and how many times?",
        "<code>find</code> returns a position or <code>-1</code>. <code>index</code> does the same but raises an error when missing. <code>count</code> counts matches.") +
        cell("s = 'banana'\nprint(s.find('an'))\nprint(s.find('z'))\nprint(s.count('a'))\nprint(s.count('an'))\nprint(s.index('n'))") +
        tip("Test with <code>find(...) != -1</code> or simply <code>'an' in s</code> when you only need yes or no.")))
    S.append(scene("Topic 3: Checking Text", head("Topic 3 · Check", "startswith, endswith, isdigit, isalpha",
        "These return <code>True</code> or <code>False</code>. They are the building blocks of simple validation.") + grid(2, [
            cell("file = 'orders_2026.csv'\nprint(file.endswith('.csv'))\nprint(file.startswith('orders'))\nprint('9876543210'.isdigit())\nprint('98765 43210'.isdigit())"),
            cell("print('Gwalior'.isalpha())\nprint('Gwalior1'.isalnum())\nprint('Gwalior1'.isalpha())\nprint('abc'.islower(), 'ABC'.isupper())"),
        ]) + warn("<code>'12.5'.isdigit()</code> is <b>False</b> because of the dot, and <code>'-5'.isdigit()</code> is False because of the minus. For decimals, try <code>float()</code> and catch the error (topic 25).")))
    S.append(scene("Chaining Methods", head("Topic 3 · Combine", "Each method returns text, so call the next one on it",
        "Read a chain from left to right: the result of one step is the input of the next.") +
        cell("raw = '   priya SHARMA \\n'\nname = raw.strip().title()\nprint(name)\n\nphone = '+91 98765-43210'\nprint(phone.replace('+91', '').replace('-', '').replace(' ', ''))") +
        tip("If a chain gets too long to read, split it over two lines or two variables. Clear beats clever.")))
    S.append(scene("Topic 4: f-strings", head("Topic 4 · Formatting", "Put values inside text with f'...{value}...'",
        "Put an <code>f</code> before the quote and write any expression inside <code>{ }</code>.") + grid(2, [
            cell("name = 'Priya'\ncity = 'Gwalior'\nqty, price = 3, 499\nprint(f'{name} from {city}')\nprint(f'{qty} x {price} = {qty * price}')\nprint(f'{name.upper()} bought {qty} items')", vars=True),
            cell("x = 42\nprint(f'{x=}')\nprint(f'{{braces}} need doubling')\nprint(f'Quote: {\"hi\"}')"),
        ]) + tip("<code>{x=}</code> prints the name and the value: a very fast way to debug.")))
    S.append(scene("f-strings: Width, Decimals, Thousands", head("Topic 4 · Formatting", "After a colon, say how to show it",
        "<code>{value:format}</code>. The format says width, alignment, decimals and thousands separator.") + grid(2, [
            cell("price = 125812.074\nprint(f'{price:.2f}')\nprint(f'{price:,.2f}')\nprint(f'{0.1834:.1%}')\nprint(f'{42:05d}')\nprint(f'{1234567:,}')"),
            cell("print(f'[{\"left\":<10}]')\nprint(f'[{\"right\":>10}]')\nprint(f'[{\"mid\":^10}]')\nprint(f'[{\"x\":*^9}]')\nprint(f'{499:>8}')"),
        ]) + warn("The comma separator is western grouping: <code>1,258,120</code>. Python has no built-in lakh grouping like <code>12,58,120</code>, so for lakh style we write a small helper later.")))
    S.append(scene("format() and the Old % Style", head("Topic 4 · Formatting", "You will see these in older code",
        "Same results, older syntax. Read them, but write f-strings.") +
        cell("print('{} bought {}'.format('Priya', 3))\nprint('{1} / {0}'.format('a', 'b'))\nprint('{:.2f}'.format(499))\nprint('%s bought %d items for %.2f' % ('Priya', 3, 1497))") +
        tip("<code>%s</code> text, <code>%d</code> whole number, <code>%.2f</code> two decimals. Still common in logging code.")))
    S.append(scene("Mistake: Methods Return New Text", mistake("Common mistake", "The result was thrown away",
        "Strings cannot change, so a method never edits the original. If you do not save the result, nothing changed.",
        "city = '  gwalior '\ncity.strip()\ncity.title()\nprint(repr(city))", None,
        "city = '  gwalior '\ncity = city.strip().title()\nprint(repr(city))",
        "Assign the result back (<code>city = city.strip()</code>). This is the number one string mistake of beginners.")))
    S.append(scene("Mistake: split(' ') vs split()", mistake("Common mistake", "Two spaces make an empty piece",
        "<code>split(' ')</code> cuts at every single space. <code>split()</code> with nothing inside splits on any run of spaces and ignores the ends.",
        "s = 'a  b   c'\nprint(s.split(' '))\nprint(len(s.split(' ')))", None,
        "s = 'a  b   c'\nprint(s.split())\nprint(len(s.split()))",
        "To split a sentence into words, use <code>split()</code> with no argument.")))
    S.append(scene("Mistake: index() Raises, find() Does Not", mistake("Common mistake", "ValueError: substring not found",
        "<code>find</code> quietly returns <code>-1</code>. <code>index</code> stops the program when the text is missing.",
        "s = 'RetailMart'\nprint(s.index('z'))", "ValueError",
        "s = 'RetailMart'\nprint(s.find('z'))\nprint('z' in s)",
        "Use <code>find</code> or <code>in</code> when the text may be absent. Remember <code>find</code> gives <code>-1</code>, which is a valid-looking index.")))
    S.append(scene("Mistake: Forgot the f", mistake("Common mistake", "{price} printed as it is",
        "Without the <code>f</code> prefix the braces are just text. Also keep the quotes inside the braces different from the outer ones.",
        "price = 499\nprint('Total: {price}')\nprint('Total: ' + price)", "TypeError",
        "price = 499\nprint(f'Total: {price}')\nprint('Total: ' + str(price))",
        "If you see <code>{price}</code> in your output, you forgot the <code>f</code>. Use <code>'single'</code> outside and <code>\"double\"</code> inside, or the other way round.")))
    S.append(scene("Real World: Tidy a Customer Name", head("Real world", "Clean a name typed three different ways",
        "Strip the spaces, fix the capitals and squash double spaces in the middle.") +
        cell("raw = '   pRIYA    sharma  '\nname = ' '.join(raw.split()).title()\nprint(repr(raw))\nprint(repr(name))\nfirst, last = name.split(' ')\nprint(last + ', ' + first)", vars=True) +
        tip("<code>' '.join(s.split())</code> is the standard trick to collapse any run of spaces into one.")))
    S.append(scene("Real World: Parse a Line of Data", head("Real world", "One line, three fields",
        "A line arrives as <code>'name,city,amount'</code> text. Split it, clean each part and turn the amount into a number.") +
        cell("line = ' priya , GWALIOR , 1,499 '\nparts = [p.strip() for p in line.split(' , ')]\nprint(parts)\nname, city, amount = parts\nprint(name.title(), city.title(), amount)", vars=True, rows=6) +
        tip("A comma inside a number (<code>1,499</code>) is a classic CSV trap. Topic 24 shows the safe way to read CSV.")))
    S.append(scene("Real World: Print an Invoice", head("Real world", "Aligned columns with f-strings",
        "Width and alignment turn lines of text into a neat table.") +
        cell("items = [('Samsung Animi Max', 2, 125812.07), ('Cable', 3, 199.0)]\nprint(f'{\"Item\":<20}{\"Qty\":>4}{\"Amount\":>16}')\nprint('-' * 40)\nfor name, qty, price in items:\n    print(f'{name:<20}{qty:>4}{qty * price:>16,.2f}')", rows=7) +
        tip("A <code>for</code> loop repeats the print for each item. You will learn it in topic 13; for now just read it.")))
    P1 = [
        practice("Easy", "Clean <code>'  gwalior '</code> into <code>Gwalior</code> and print it.", "print()", "Gwalior", "print('  gwalior '.strip().title())"),
        practice("Easy", "Print <code>'retailmart'</code> in capitals.", "print()", "RETAILMART", "print('retailmart'.upper())"),
        practice("Medium", "Print the city (the middle part) of the line.", "line = 'Priya,Gwalior,499'\nprint()", "Gwalior", "line = 'Priya,Gwalior,499'\nprint(line.split(',')[1])"),
        practice("Medium", "Use an f-string to print <code>Samsung Animi Max: ₹125,812.07</code>.", "name = 'Samsung Animi Max'\nprice = 125812.07\nprint()", "Samsung Animi Max: ₹125,812.07", "name = 'Samsung Animi Max'\nprice = 125812.07\nprint(f'{name}: ₹{price:,.2f}')"),
    ]
    P2 = [
        practice("Hard", "Predict first, then print the number of pieces from <code>split(' ')</code> and from <code>split()</code> on one line.", "s = 'a  b   c'\nprint()", "6 3", "s = 'a  b   c'\nprint(len(s.split(' ')), len(s.split()))"),
        practice("Hard", "Predict first, then print <code>count('an')</code>, <code>find('n')</code> and <code>find('z')</code> of <code>'banana'</code> on one line.", "s = 'banana'\nprint()", "2 2 -1", "s = 'banana'\nprint(s.count('an'), s.find('n'), s.find('z'))"),
        practice("Crazy", "Clean the messy name into <code>Priya Sharma</code> and print it.", "raw = ' PRIYA sharma '\nprint()", "Priya Sharma", "raw = ' PRIYA sharma '\nprint(raw.strip().title())"),
        practice("Crazy", "Turn the date <code>2026-11-22</code> into <code>22-11-2026</code> using <code>split</code>, a reversed slice and <code>join</code>.", "d = '2026-11-22'\nprint()", "22-11-2026", "d = '2026-11-22'\nprint('-'.join(d.split('-')[::-1]))"),
    ]
    S.append(scene("Practice Arena: Easy and Medium", head("Practice Arena", "Easy and Medium", "Type the answer, press Run. Green means correct.") + grid(2, P1)))
    S.append(scene("Practice Arena: Hard and Crazy", head("Practice Arena", "Hard and Crazy", "Predict before you run. These are the traps interviewers like.") + grid(2, P2)))
    S.append(scene("Interview Studio", head("Interview Studio", "Five questions interviewers ask about string methods") + grid(2, [
        reveal("Why does s.upper() not change s?", "Strings are immutable, so every method returns a <b>new</b> string. Save it: <code>s = s.upper()</code>."),
        reveal("What is the difference between split() and split(' ')?", "<code>split(' ')</code> cuts at every single space, so double spaces give empty pieces. <code>split()</code> splits on any run of whitespace and drops empty pieces."),
        reveal("find() versus index()?", "Both return the position. When the text is missing, <code>find</code> returns <code>-1</code> and <code>index</code> raises <code>ValueError</code>."),
        reveal("How do you put a number with 2 decimals and a comma into text?", "<code>f'{value:,.2f}'</code>. For example <code>f'{125812.07:,.2f}'</code> gives <code>125,812.07</code>."),
        reveal("How do you join a list of words into one sentence?", "<code>' '.join(words)</code>. The separator calls <code>join</code>, and the list goes inside the brackets. Items must already be strings."),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these without running code?", "Click a card to check yourself.") + grid(3, [
        reveal("<code>'  hi '.strip()</code>?", "<code>'hi'</code>."),
        reveal("<code>'a,b,c'.split(',')</code>?", "<code>['a', 'b', 'c']</code>."),
        reveal("<code>'-'.join(['x', 'y'])</code>?", "<code>'x-y'</code>."),
        reveal("<code>'Python'.find('z')</code>?", "<code>-1</code>."),
        reveal("<code>f'{3.14159:.2f}'</code>?", "<code>'3.14'</code>."),
        reveal("<code>'123'.isdigit()</code>?", "<code>True</code>."),
    ])))
    S.append(scene("Key Takeaways", head("Key Takeaways", "Six rules to remember") + grid(3, [
        card("blue", "1 · Methods return new text", '<p>Assign the result: <code>s = s.strip()</code>.</p>'),
        card("green", "2 · Clean, then compare", '<p><code>strip().lower()</code> before you compare or count.</p>'),
        card("orange", "3 · split and join", '<p>Cut with <code>split(sep)</code>, glue with <code>sep.join(list)</code>.</p>'),
        card("red", "4 · split() vs split(' ')", '<p>No argument handles any run of spaces.</p>'),
        card("purple", "5 · f-strings", '<p><code>f\'{x:,.2f}\'</code> for money. <code>{x=}</code> to debug.</p>'),
        card("blue", "6 · find vs index", '<p><code>find</code> gives -1, <code>index</code> raises an error.</p>'),
    ])))
    def qr(t, code): return f'<div><h3>{t}</h3>{cell(code)}</div>'
    S.append(scene("Quick Reference", head("Quick Reference", "Every syntax from today") + grid(3, [
        qr("Case and clean", "s = '  gwalior '\nprint(s.strip().title(), s.upper())"),
        qr("Split and join", "p = 'a,b,c'.split(',')\nprint(p, '-'.join(p))"),
        qr("Replace", "print('1,499'.replace(',', ''))"),
        qr("Search", "s = 'banana'\nprint(s.find('an'), s.count('a'))"),
        qr("Check", "print('a.csv'.endswith('.csv'), '42'.isdigit())"),
        qr("f-string", "price = 125812.07\nprint(f'Rs {price:,.2f}')"),
    ])))
    S.append(scene("Take-Home Challenge", head("Take-Home Challenge", "Clean a customer record",
        "Raw record: <code>'  rAHUL verma ;; GWALIOR ;; 2,499.50 '</code>. Work in the cell below, then check against a classmate or in a 1:1.") + grid(2, [
        '<div class="card"><ol style="padding-left:20px;color:var(--muted);line-height:1.9"><li>Split the record on <code>;;</code> into name, city and amount.</li><li>Clean each part (strip and fix capitals).</li><li>Turn the amount into a number (remove the comma first).</li><li>Print one line: <code>Rahul Verma from Gwalior paid ₹2,499.50</code> with an f-string.</li><li>Print the initials, <code>R.V.</code>, using indexing.</li></ol></div>',
        cell("# your work here\nrecord = '  rAHUL verma ;; GWALIOR ;; 2,499.50 '\n", vars=True, rows=10),
    ])))
    import curriculum_data
    topics = [t["title"] for t in curriculum_data.MODULES[1]["topics"] if t["n"].isdigit()]
    j = "".join(f'<span class="{"here" if i == 4 else ("done" if i < 4 else "")}">{i+1}. {t}</span>' for i, t in enumerate(topics))
    S.append(scene("Your Python Journey", head("Your Python journey", "Module 1: Python Foundations", "You are here: topic 5 of 29.") + f'<div class="journey">{j}</div>'))
    S.append(scene("Next: Booleans, Comparison & Logic", head("Next topic", "Booleans, Comparison &amp; Logic",
        "True and False, comparison, <code>and</code> / <code>or</code> / <code>not</code>, and why <code>None</code> is not SQL's NULL. Conditions come next.") +
        '<div class="mission"><b>Before the next topic:</b> finish the take-home and try it in the playground: <a href="/playground/">python.theshiraverse.com/playground</a></div>'
        '<div style="margin-top:20px"><span class="chip"><b>Next:</b> Booleans, Comparison &amp; Logic (coming soon)</span></div>'))
    return S
