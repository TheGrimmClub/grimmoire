# 10 · Tooling · uv

> The modern way to manage Python, packages, and projects — one fast tool.

So far you've run single files. Real projects need more: the right Python
version, extra libraries, and a way to keep it all reproducible so it works on
*everyone's* machine. That's what [uv](https://docs.astral.sh/uv) is for.

## What you'll learn

- What **uv** is and why the club uses it
- Installing Python without fighting your system
- Starting a project and adding dependencies
- Running code inside the project's environment

## What uv is

`uv` is a single, very fast tool (written in Rust) that replaces the old tangle
of `pip`, `venv`, `pyenv` and friends. It was installed on day one in
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup).

```sh
uv --version
```

## Managing Python itself

uv can install Python for you — no system mess:

```sh
uv python install 3.13     # download and install Python 3.13
uv python list             # see what's installed
```

!!! note "Why not the system Python?"
    - macOS ships an old Python meant for the operating system — don't touch it.
    - Linux ties Python to system packages; upgrading can break things.
    - Windows has no Python at all by default.

    uv gives every club member the **same** interpreter, isolated and
    reproducible.

## A project in four commands

```sh
uv init grimm-first     # 1. make a project (creates pyproject.toml + main.py)
cd grimm-first
uv add rich             # 2. add a dependency (records it + a lockfile)
uv run main.py          # 3. run inside the project's own environment
uv sync                 # 4. (re)install everything from the lockfile
```

`uv run` is the magic one: it makes sure the environment is ready, then runs your
code with exactly the right Python and libraries — no "works on my machine"
surprises.

!!! tip "The lockfile"
    `uv add` writes an exact recipe (`uv.lock`) of every package and version.
    Commit it, and a teammate's `uv sync` reproduces your environment byte for
    byte.

## Worked example

```sh
uv init grimm-first
cd grimm-first
uv add rich
```

Put this in `main.py`:

```python
from rich import print

print("[bold magenta]Willkommen im Grimm Club![/]")
```

Run it:

```sh
uv run main.py
```

You just used a third-party library, installed and wired up by uv, with colour in
your terminal.

## Try it

!!! example "Übung — a coloured hero"
    In your `grimm-first` project, `uv add rich`, then print your hero's name in a
    colour of your choice using `from rich import print` and `[colour]...[/]`.

??? tip "Hint"
    ```python
    from rich import print
    print("[green]Hänsel[/] betritt den Wald.")
    ```

## Recap

- **uv** manages Python versions, dependencies, and environments — one tool.
- Install Python *through* uv, not the system, for the same setup everywhere.
- `uv init` → `uv add` → `uv run` → `uv sync` is the everyday loop.

## Cheat sheet

| Command | Does |
|---------|------|
| `uv python install 3.13` | install a Python version |
| `uv init NAME` | start a project |
| `uv add PKG` | add a dependency |
| `uv run FILE` | run in the project env |
| `uv sync` | install everything from the lockfile |

---

**Next:** [11 · Create Your Package](11-create-your-package.md).
