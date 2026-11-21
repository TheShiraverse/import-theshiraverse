from deck_lib import *

META = dict(
    path="get-started/set-up-python", title="Set Up Python on Your Laptop", tag="Get started · Part 4 of 5",
    desc="Get started, part 4 of 5: install Python and VS Code on Windows or Mac, create a virtual environment, install packages with pip, and run Jupyter.",
    mission_label="In this part", mission="get Python, VS Code and Jupyter working in a clean environment, step by step, on Windows or Mac.",
    pyrun='{base:"/playground/",data:false,packages:[]}',
)

def build():
    S = []
    S.append(agenda([("Install", ["Python on Windows or Mac", "VS Code and its Python extension", "Anaconda as an alternative"]),
                     ("Environments and packages", ["Virtual environments (venv)", "pip: install, list, freeze", "requirements.txt"]),
                     ("Run and fix", ["Your first script", "Jupyter", "Common problems and fixes"])]))
    S.append(scene("The Plan", head("Overview", "Five steps, about thirty minutes", "Do them in order. Each step has a check so you know it worked.") + grid(5, [
        card("blue", "1 · Python", "<p>Install it and check the version.</p>"),
        card("green", "2 · VS Code", "<p>A free editor with a Python extension.</p>"),
        card("orange", "3 · Environment", "<p>A private folder of packages for this course.</p>"),
        card("purple", "4 · Packages", "<p>Install pandas, matplotlib and Jupyter with pip.</p>"),
        card("red", "5 · Run", "<p>Run a script and a notebook.</p>"),
    ]) + tip("Terminal commands are in dark boxes with a <b>Copy</b> button. Run them in a terminal, not in the browser cells.")))
    S.append(scene("Step 1 · Install Python", head("Step 1", "Install Python (Windows and Mac)", "Get it from python.org/downloads. Python 3.15 is the latest at the time of writing; any recent 3.x works for this course.") + '<div class="os">'
        '<div class="card blue"><span class="k">Windows</span><ul><li>Download the <b>Python install manager</b> from python.org/downloads, or get it from the Microsoft Store.</li><li>Install it, then open a <b>new</b> terminal (PowerShell).</li><li>The commands <code>python</code>, <code>py</code> and <code>pymanager</code> should now exist.</li></ul>' + term("py -3 --version\npy list", "Check (PowerShell)") + '</div>'
        '<div class="card green"><span class="k">Mac</span><ul><li>Download <b>Python for macOS</b> (.pkg) from python.org/downloads and open it.</li><li>Then open the folder <code>/Applications/Python 3.15/</code> and double-click <b>Install Certificates.command</b>.</li><li>Do not use or modify the older Python that Apple ships.</li></ul>' + term("python3 --version", "Check (Terminal)") + '</div></div>'
        + tip("You should see a version starting with <b>3</b>. If you see 2.x, or the command is not found, jump to the problems table later in this page.")))
    S.append(scene("Alternative: Anaconda", head("Step 1 (alternative)", "Anaconda or Miniconda", "A bundle that installs Python and manages environments for you. Choose it or plain Python, not both.") + grid(2, [
        card("blue", "Use it if", "<ul><li>You want one installer that includes data tools</li><li>Your team or college already uses conda</li></ul>"),
        card("green", "Create an environment", term("conda create --name ds_env python\nconda activate ds_env\nconda install pandas matplotlib jupyterlab", "Terminal (Anaconda Prompt on Windows)")),
    ]) + warn("Do not mix pip and conda for the same package in one environment. Pick one way and stay with it.")))
    S.append(scene("Step 2 · VS Code", head("Step 2", "Install VS Code and the Python extension", "VS Code is a free editor from Microsoft. Download it from code.visualstudio.com.") + grid(3, [
        card("blue", "Install the extension", "<p>Open Extensions, search <b>Python</b>, install the one by <b>ms-python</b> (id <code>ms-python.python</code>). It does not include Python itself, which you installed in step 1.</p>"),
        card("green", "Pick the interpreter", "<p>Open the Command Palette (<b>Ctrl+Shift+P</b> on Windows, <b>Cmd+Shift+P</b> on Mac) and run <b>Python: Select Interpreter</b>.</p>"),
        card("purple", "Open a terminal", "<p>Use <b>Terminal &rarr; New Terminal</b> inside VS Code so your commands run in your project folder.</p>"),
    ]) + tip("Open a <b>new</b> terminal after installing Python so it picks up the changes.")))
    S.append(scene("Step 3 · Virtual Environment", head("Step 3", "A virtual environment keeps this course tidy",
        "An environment is a private folder with its own Python and its own packages. Projects never fight over versions. Make one inside your project folder.") + '<div class="os">'
        '<div class="card blue"><span class="k">Windows (PowerShell)</span>' + term("py -3 -m venv .venv\n.venv\\Scripts\\Activate.ps1", "Create and activate") + '<p style="margin-top:8px">If PowerShell says scripts are disabled, run this once:</p>' + term("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser", "PowerShell, once") + '</div>'
        '<div class="card green"><span class="k">Mac and Linux</span>' + term("python3 -m venv .venv\nsource .venv/bin/activate", "Create and activate") + '<p style="margin-top:8px">Leave the environment any time with:</p>' + term("deactivate", "Both systems") + '</div></div>'
        + tip("When it is active, your prompt starts with <b>(.venv)</b>. If you do not see it, you are not inside the environment.")))
    S.append(scene("Step 4 · pip", head("Step 4", "Install packages with pip", "pip downloads packages from the Python Package Index. Always run it as <code>python -m pip</code> so it uses the Python you think it does.") + grid(2, [
        card("blue", "Install what the course needs", term("python -m pip install pandas matplotlib jupyterlab", "With the environment active")),
        card("green", "Check it worked", term('python -c "import pandas; print(pandas.__version__)"', "Prints a version number")),
        card("purple", "See and share your packages", term("python -m pip list\npython -m pip freeze > requirements.txt", "List, then save")),
        card("orange", "Rebuild elsewhere / remove", term("python -m pip install -r requirements.txt\npython -m pip uninstall pandas", "Install from the list / uninstall")),
    ])))
    S.append(scene("Step 5 · Run Something", head("Step 5", "Run a script and open Jupyter", "Create a file called <code>hello.py</code> in VS Code with one line, then run it from the terminal.") + grid(2, [
        card("blue", "A script", cell("print('Hello, TheShiraverse')", label="Try here") + term("python hello.py", "In your terminal")),
        card("green", "A notebook", "<p>Either run Jupyter in the browser:</p>" + term("jupyter lab", "Opens a page in your browser") + "<p style='margin-top:8px'>or in VS Code create a file named <code>hello.ipynb</code>, choose your <b>.venv</b> kernel, and run a cell.</p>"),
    ])))
    S.append(scene("Common Problems", head("Troubleshooting", "If something goes wrong, check this table first") + table(["What you see", "Likely cause", "Fix"], [
        ["<code>python</code> not found", "On Mac the command is <code>python3</code>; on Windows the terminal was open before the install", "Use <code>python3</code> (Mac) or <code>py</code> (Windows); open a new terminal"],
        ["pip installs, but <code>import</code> fails", "pip belongs to a different Python than the one running your code", "Always use <code>python -m pip install ...</code> with the environment active"],
        ["No <code>(.venv)</code> in the prompt", "The environment is not active", "Run the activate command again from the project folder"],
        ["PowerShell: running scripts is disabled", "Windows blocks activation scripts by default", "Run the <code>Set-ExecutionPolicy ... RemoteSigned</code> command once"],
        ["Mac: SSL certificate error", "Certificates not installed after the python.org installer", "Run <b>Install Certificates.command</b> in <code>/Applications/Python 3.15/</code>"],
        ["VS Code uses the wrong Python", "Wrong interpreter selected", "Command Palette &rarr; <b>Python: Select Interpreter</b> &rarr; pick the <b>.venv</b> one"]])))
    S.append(scene("Self-Check", head("Self-Check", "Can you answer these?", "Click a card to check yourself.") + grid(3, [
        reveal("How do you check which Python version you have?", "Mac: <code>python3 --version</code>. Windows: <code>py -3 --version</code>."),
        reveal("Why use a virtual environment?", "Each project gets its own Python and packages, so versions never clash."),
        reveal("How do you know the environment is active?", "The prompt starts with <code>(.venv)</code>."),
        reveal("Why <code>python -m pip</code> instead of just <code>pip</code>?", "It guarantees pip belongs to the same Python that will run your code."),
        reveal("How do you save and restore your package list?", "<code>pip freeze &gt; requirements.txt</code>, then <code>pip install -r requirements.txt</code>."),
        reveal("Which VS Code extension do you need?", "Python by ms-python (<code>ms-python.python</code>)."),
    ])))
    S.append(closing("Website walkthrough", "/notes/get-started/website-walkthrough/", "A quick tour of the notes, playground, practice and where to get help."))
    return S
