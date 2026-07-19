# Setup 3 · Test Your Installation

> Proving the workbench works — a real project, a real file, a real run.

Two commands answered you politely. That isn't proof. This chapter builds
something small and runs it, so you start Chapter 01 knowing your tools work
rather than hoping they do.

## What you'll learn

- Making your first project with `uv init`
- Writing a file and running it with `uv run`
- Reading an error message instead of fearing it
- The three things that go wrong on day one

## Make a project

```sh
uv init grimm-first
cd grimm-first
```

`uv init` makes a folder with a few files in it. Two matter today:

- `pyproject.toml` — the project's name card. It says what this project is and
  what it needs.
- `main.py` — a starter Python file, with a `print(...)` already in it.

You'll meet the rest in [10 · Tooling · uv](10-tooling-uv.md) and build one
properly in [11 · Create Your Package](11-create-your-package.md).

## Run it

```sh
uv run main.py
```

```
Hello from grimm-first!
```

That output is the whole point of the setup chapter. Python is installed, the
project is real, and `uv run` connected the two.

!!! note "What `uv run` just did"
    It checked the project had an environment, made one if not, and then ran
    your file inside it. That's why you never had to "activate" anything.

## Write your own

Open `main.py` in your editor — [micro](https://micro-editor.github.io) if you
followed GrimmSetup — and replace it with:

```python
print("The forest is dark, but the path is lit.")
```

```sh
uv run main.py
```

```
The forest is dark, but the path is lit.
```

You just wrote and ran your own Python. Everything after this is detail.

## When it goes wrong

It will, and that's ordinary. The three from day one:

**`command not found: uv`** — the shell can't see uv. Open a new window; see
[Setup 1](a__01-setup-uv.md).

**`No such file or directory: main.py`** — you're in the wrong folder. Ask where
you are with `pwd`, and list what's there with `ls`. You need to be *inside*
`grimm-first`.

**`SyntaxError`** — a typo in the Python itself. Almost always a missing quote or
bracket. Python prints the line number and points a `^` at the spot:

```
  File "main.py", line 1
    print("The forest is dark)
          ^
SyntaxError: unterminated string literal
```

!!! tip "Errors are directions, not verdicts"
    An error message is Python telling you exactly where it got confused. Read
    it from the **bottom up**: the last line says what went wrong, the lines
    above say where. This is a skill, and you start building it now — you'll
    sharpen it properly in [05 · Debugger](05-debugger.md).

## Recap

- `uv init <name>` starts a project; `uv run <file>` runs code inside it.
- `pyproject.toml` is the project's name card.
- Errors name the file, the line and the problem — read them bottom up.

## Cheat sheet

| You want to… | Command |
|--------------|---------|
| Start a project | `uv init grimm-first` |
| Run a file | `uv run main.py` |
| Where am I? | `pwd` |
| What's here? | `ls` |

---

The workbench is ready. Time for the first spell.

**Next:** [01 · Commands & Calls](01-commands-and-calls.md) — talking to the machine.
