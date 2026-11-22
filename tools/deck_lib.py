"""Scene helpers for Nukte decks of the Python course. Every runnable cell is verified at build time."""
import html, io, contextlib, traceback

CELLS = []   # (scene_title, code, raises, expect)

def e(s): return html.escape(s, quote=True)

def cell(code, vars=False, raises=None, expect=None, rows=None, autoexpect=False, label="Run"):
    """A runnable cell. raises='TypeError' marks a cell that must fail with that error.
    expect='text' turns it into a practice cell (checked in the browser and at build time against the solution)."""
    code = code.strip("\n")
    n = rows or max(2, code.count("\n") + 1)
    CELLS.append({"code": code, "raises": raises, "expect": expect})
    attrs = (' data-vars' if vars else '') + (f' data-expect="{e(expect)}"' if expect is not None else '')
    return (f'<div class="cell"{attrs}><textarea class="code" rows="{n}" spellcheck="false" aria-label="Python code">{e(code)}</textarea>'
            f'<div class="cellbar"><button class="run" type="button">&#9654; {label}</button><button class="copy" type="button">Copy</button>'
            f'<button class="reset" type="button">Reset</button><span class="st"></span></div>'
            f'<div class="out" aria-live="polite"></div><div class="vars"></div></div>')

def scene(title, body, cls=""):
    return f'<section class="scene {cls}" data-title="{e(title)}"><div class="inner">{body}</div></section>'

def title_scene(tag, title, summary, chips, mission):
    ch = "".join(f'<span class="chip"><b>{n}</b> {l}</span>' for n, l in chips)
    return ("TITLE", tag, title, summary, ch, mission)

def card(kind, k, body): return f'<div class="card {kind}"><span class="k">{k}</span>{body}</div>'
def grid(n, items): return f'<div class="grid g{n}">{"".join(items)}</div>'
def tip(t): return f'<div class="tip"><b>Pro tip.</b> {t}</div>'
def warn(t): return f'<div class="warn"><b>Watch out.</b> {t}</div>'
def head(tag, h, lead=""): return f'<div class="tag">{tag}</div><h2>{h}</h2>' + (f'<p class="lead">{lead}</p>' if lead else '')

def mistake(tag, h, lead, broken_code, raises, fixed_code, why):
    return (head(tag, h, lead) + '<div class="grid g2"><div><div class="label r">Broken</div>' + cell(broken_code, raises=raises) +
            '</div><div><div class="label g">Fixed</div>' + cell(fixed_code) + '</div></div>' + warn(why))

def practice(tier, ask, starter, expect, solution):
    CELLS.append({"code": solution, "raises": None, "expect": expect, "practice": True})
    c = cell(starter, expect=expect).replace("<div class=\"cell\"", "<div class=\"cell\"", 1)
    CELLS.pop()   # the starter is not run at build time; the solution is
    return (f'<div><span class="arena-tier t-{tier.lower()}">{tier}</span><p class="ask">{ask}</p>{c}'
            f'<div class="reveal" style="margin-top:10px;padding:10px 14px"><button class="rv" type="button" data-label="Show solution">Show solution</button>'
            f'<div class="answer"><code style="white-space:pre-wrap;display:block">{e(solution)}</code></div></div></div>')

def reveal(q, a): return f'<div class="reveal"><div class="q">{q}</div><button class="rv" type="button" data-label="Show answer">Show answer</button><div class="answer">{a}</div></div>'

def verify_cells():
    """Run every cell once in a fresh namespace (Python on this Mac). Raises on a wrong result."""
    problems = []
    for c in CELLS:
        import sys
        buf = io.StringIO(); g = {"__name__": "__main__"}; err = None
        old_stdin = sys.stdin; sys.stdin = io.StringIO("")   # input() must not wait on the terminal
        try:
            with contextlib.redirect_stdout(buf):
                import ast
                tree = ast.parse(c["code"]); last = None
                if tree.body and isinstance(tree.body[-1], ast.Expr): last = ast.Expression(tree.body.pop().value)
                exec(compile(tree, "<c>", "exec"), g)
                if last is not None:
                    v = eval(compile(last, "<c>", "eval"), g)
                    if v is not None: buf.write(repr(v))
        except BaseException as ex:
            err = type(ex).__name__
        finally:
            sys.stdin = old_stdin
        out = buf.getvalue().strip()
        if c["raises"] == "*":
            if not err: problems.append(f'expected an error, got none: {c["code"][:50]!r}')
        elif c["raises"]:
            if err != c["raises"]: problems.append(f'expected {c["raises"]}, got {err}: {c["code"][:50]!r}')
        elif err: problems.append(f'unexpected {err}: {c["code"][:60]!r}')
        elif c["expect"] is not None and out != c["expect"].strip():
            problems.append(f'solution gives {out!r}, expect {c["expect"]!r}: {c["code"][:60]!r}')
    return problems


def term(cmds, label="Terminal"):
    """A terminal-command block with a Copy button (not run in the browser, not verified at build time)."""
    body = e(cmds.strip("\n"))
    return (f'<div class="term"><div class="termbar"><span>{e(label)}</span><button class="copy2" type="button" data-copy="{body}">Copy</button></div>'
            f'<pre>{body}</pre></div>')

def pillars(items):
    out = "".join(f'<div class="pillar"><div class="n">0{i+1}</div><h3>{t}</h3><ul>' + "".join(f"<li>{x}</li>" for x in lis) + "</ul></div>" for i, (t, lis) in enumerate(items))
    return f'<div class="grid g{len(items)}">{out}</div>'

def agenda(items): return scene("Today's Agenda", head("Agenda", "What we cover") + pillars(items))

def table(headers, rows, cls="map"):
    h = "".join(f"<th>{x}</th>" for x in headers)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="card"><table class="{cls}"><tr>{h}</tr>{r}</table></div>'

def closing(next_title, next_href, blurb, links=True):
    nxt = f'<a class="btn-next" href="{next_href}">Next: {next_title} &rarr;</a>' if next_href else f'<span class="chip"><b>Next:</b> {next_title} (coming soon)</span>'
    return scene("Next", head("Next", next_title, blurb) + f'<div style="margin-top:18px">{nxt}</div>')
