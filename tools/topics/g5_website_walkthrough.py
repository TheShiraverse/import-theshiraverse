from deck_lib import *

META = dict(
    path="get-started/website-walkthrough", title="Website Walkthrough", tag="Get started · Part 5 of 5",
    desc="Get started, part 5 of 5: a quick tour of the Nukte notes, the playground, the curriculum and where to get help, plus a simple routine for studying each topic.",
    mission_label="In this part", mission="know where everything is on the site and how to study each topic.",
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(agenda([("Where things are", ["Home and the curriculum", "Nukte notes", "The playground"]),
                     ("How a topic works", ["Scenes and keyboard keys", "Runnable cells and practice", "Order of topics"]),
                     ("Study and get help", ["A six-step routine", "Book a 1:1", "Community"])]))
    S.append(scene("The Site Map", head("Part 1 · Where things are", "Four places you will use", "Everything lives at python.theshiraverse.com.") + grid(4, [
        card("blue", "Home", "<p>The curriculum map, the Get started sections, and links to the other courses.</p><p><a href=\"/\">Open</a></p>"),
        card("green", "Nukte notes", "<p>One slide-style lesson per topic, with live code. This is the main place you learn.</p><p><a href=\"/notes/\">Open</a></p>"),
        card("purple", "Playground", "<p>A blank page to experiment on, with pandas and sample tables.</p><p><a href=\"/playground/\">Open</a></p>"),
        card("orange", "SQL course", "<p>The sister course. Python topics point back to it often.</p><p><a href=\"https://sql.theshiraverse.com\">Open</a></p>"),
    ])))
    S.append(scene("Inside a Nukte Deck", head("Part 2 · How a topic works", "Every topic is a deck of scenes", "You are inside one right now.") + grid(2, [
        card("blue", "Move around", "<ul><li><b>&rarr;</b> or <b>Space</b>: next scene</li><li><b>&larr;</b>: previous scene</li><li><b>M</b> or the Scenes button: jump to any scene</li><li>The bar at the bottom shows your progress</li></ul>"),
        card("green", "What a topic contains", "<ul><li>A story and the SQL connection</li><li>Explanations with runnable cells</li><li>Common mistakes: broken and fixed</li><li>A practice arena, interview questions, a self-check</li><li>Key takeaways, a quick reference and a take-home</li></ul>"),
    ]) + '<div style="margin-top:20px">' + cell("print('Try pressing M to see every scene in this deck')") + '</div>'))
    S.append(scene("Practice", head("Part 2 · How a topic works", "Practice is built into each topic", "Each topic ends with a Practice Arena in four levels.") + grid(4, [
        '<div class="card"><span class="arena-tier t-easy">Easy</span><p>One idea, one line.</p></div>',
        '<div class="card"><span class="arena-tier t-medium">Medium</span><p>Two ideas together.</p></div>',
        '<div class="card"><span class="arena-tier t-hard">Hard</span><p>The traps interviewers like.</p></div>',
        '<div class="card"><span class="arena-tier t-crazy">Crazy</span><p>Predict before you run.</p></div>',
    ]) + '<div style="margin-top:20px">' + cell("# type the answer, press Run: green means correct\nprint(2 ** 10)", expect="1024") + '</div>'
        + tip("Separate practice banks, like the ones on the SQL site, will be added as modules are completed.")))
    S.append(scene("The Curriculum Order", head("Part 2 · How a topic works", "Follow the order", "Topics build on each other. Skip ahead only when you can already do the topic.") + table(["Module", "Starts with"], [
        ["Get started", "what Python is, how it runs, the browser, your laptop, this tour"],
        ["1 Python Foundations", "Hello Python, variables, numbers, text, lists, dictionaries, loops, functions"],
        ["2 NumPy &amp; pandas", "arrays, DataFrames, selecting, filtering, cleaning"],
        ["3 Analysis", "groupby, pivot, merge, time series, summaries"],
        ["4 to 6", "visualisation, the analyst toolkit, interview prep and a capstone"]]) +
        tip("Some topics are published before others. The notes page marks what is ready.")))
    S.append(scene("A Six-Step Routine", head("Part 3 · Study and get help", "How to study one topic", "A simple routine beats a long session.") + grid(3, [
        card("blue", "1 · Read the story", "<p>Get the big idea before the syntax.</p>"),
        card("green", "2 · Run every cell", "<p>Press Run, then change the code and run again.</p>"),
        card("purple", "3 · Break it on purpose", "<p>Cause the common mistakes and read the errors.</p>"),
        card("orange", "4 · Do the practice arena", "<p>Do Easy to Crazy without peeking at solutions.</p>"),
        card("red", "5 · Do the take-home", "<p>Use your own laptop and your own words.</p>"),
        card("blue", "6 · Teach it back", "<p>Explain it in two sentences to someone, or write it down.</p>"),
    ])))
    S.append(scene("Getting Help", head("Part 3 · Study and get help", "Stuck? You have options") + grid(2, [
        card("blue", "Book a 1:1", "<p>Stuck on a doubt, want a mock interview, or want your code reviewed?</p><p><a href=\"https://theshiraverse.com/book\">theshiraverse.com/book</a></p>"),
        card("green", "Community", "<ul><li><a href=\"https://chat.whatsapp.com/JzuixbXtgVs0u9c46GuIc0\">WhatsApp Community</a></li><li><a href=\"https://whatsapp.com/channel/0029VbCxiGiJf05eJBC59q3R\">WhatsApp Channel</a></li><li><a href=\"https://discord.gg/gABgF8P3pt\">Discord</a></li><li><a href=\"https://www.youtube.com/@theshiraverse\">YouTube</a></li></ul>"),
    ])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these?", "Click a card to check yourself.") + grid(3, [
        reveal("Which key jumps to any scene?", "<b>M</b> (or the Scenes button)."),
        reveal("Where do you try ideas on a blank page?", "The playground."),
        reveal("What are the four practice levels?", "Easy, Medium, Hard and Crazy."),
        reveal("Which comes first: the story or the syntax?", "The story. Get the idea, then the syntax."),
        reveal("What is the best way to learn a mistake?", "Cause it on purpose and read the error."),
        reveal("Where do you book a 1:1?", "theshiraverse.com/book"),
    ])))
    S.append(closing("Topic 1: Hello Python", None, "Your first program: print(), comments, syntax, indentation and style. Published soon."))
    return S
