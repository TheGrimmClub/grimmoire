# 01 · Commands & Calls

> Talking to the machine: typing commands in the shell, and calling functions in Python.

Every journey in the Grimm world starts with a single word typed into the dark.
This chapter is about that first conversation with the computer — how you give it
an instruction and how it answers back.

## What you'll learn

- What a **shell** is and how to run a command
- How to start Python and run a `.py` file
- What a **function call** looks like — `name(arguments)`
- Your first call, `print(...)`, and how to read its output
- How to fix the three mistakes everyone makes on day one

## The shell: your first doorway

The **shell** (also "terminal" or "console") is a program that waits for you to
type a **command** and press Enter. It runs the command and shows the result.
It's just a conversation: you say something, it answers.

```sh
python --version      # ask which Python you have
```

```
Python 3.13.0
```

You typed a command; the shell answered. That's the whole loop, forever.

!!! tip "Where's my shell?"
    It was set up on day one in
    [GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup), together with the
    [micro](https://micro-editor.github.io) editor. On macOS it's *Terminal*, on
    Windows the *Git Bash* shell, on Linux any terminal app.

## Running Python

There are three ways to run Python, from quickest to most useful:

```sh
python                       # 1. start an interactive session (a REPL)
python -c "print(2 + 2)"     # 2. run one line and exit
python hello.py              # 3. run a whole file
```

The **REPL** (Read–Eval–Print Loop) is a Python shell *inside* your shell. You
type Python, it answers immediately. Leave it with `exit()`.

```python
>>> 2 + 2
4
>>> exit()
```

## Calls: telling code to run

A **call** is when you tell a piece of code to do its job. You write its
**name**, then round brackets `()` with any values it needs inside:

```python
print("Hallo, Grimm Club!")
```

- `print` — the **name** of the function.
- `"Hallo, Grimm Club!"` — the **argument**, the value you hand it.
- `()` — the brackets mean *"do it now"*.

Without the brackets, you're only *pointing at* the function, not running it:

```python
print          # <built-in function print>  — nothing happens
print()        # (prints an empty line)      — it runs
```

You can pass more than one argument, separated by commas:

```python
print("HP:", 100)     # HP: 100
```

## A first file

Open your editor and make `hello.py`:

```python
print("Ich betrete den Wald.")
print("Es ist dunkel.")
```

Run it:

```sh
python hello.py
```

```
Ich betrete den Wald.
Es ist dunkel.
```

Python runs the file **top to bottom**, one line at a time. Order matters.

## Three day-one mistakes

!!! warning "Watch out"
    - **Forgetting the quotes:** `print(Hallo)` looks for a *variable* named
      `Hallo` and errors. Text needs quotes: `print("Hallo")`.
    - **Forgetting the brackets:** `print "hi"` is not a call in Python 3 — it's a
      `SyntaxError`. Always `print("hi")`.
    - **Wrong folder:** `python hello.py` only works if you're *in* the folder
      that holds `hello.py`. Use `ls` (macOS/Linux) or `dir` (Windows) to look
      around.

## Try it

!!! example "Übung 1 — your name"
    In the REPL, print your name: `print("...")`. Then print your name and your
    age on one line using a comma.

!!! example "Übung 2 — a tiny scene"
    Make a file `wald.py` with three `print(...)` lines that tell a mini scene in
    the forest. Run it with `python wald.py`.

??? tip "Stuck? A worked solution"
    ```python
    # wald.py
    print("Ich stehe am Waldrand.")
    print("Drei Männlein winken mir zu.")
    print("Ich gehe hinein.")
    ```
    ```sh
    python wald.py
    ```

## Recap

- The **shell** runs **commands**; Python runs from the REPL, `-c`, or a file.
- A **call** is `name(arguments)` — the brackets make it run *now*.
- `print(...)` shows values; text needs `"quotes"`.

## Cheat sheet

| You want to… | Command |
|--------------|---------|
| Check your Python | `python --version` |
| Start the REPL | `python` (leave with `exit()`) |
| Run one line | `python -c "..."` |
| Run a file | `python file.py` |
| Print something | `print(value)` |

---

**Next:** [02 · Imports](02-imports.md) — using code other people wrote.
