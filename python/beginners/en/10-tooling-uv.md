# 10 · Tooling · uv

> The modern way to manage Python, packages, and projects — one fast tool.

## What you'll learn

- What **uv** is and why the club uses it
- Installing Python without fighting your system
- Starting a project and adding dependencies
- Running code in the project's environment

## The idea

[uv](https://docs.astral.sh/uv) replaces the old tangle of `pip`, `venv`,
`pyenv` and friends with a single fast tool. It was installed on day one in
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup).

```sh
uv python install 3.13     # get Python itself
uv init grimm-first        # start a new project (makes pyproject.toml)
cd grimm-first
uv add requests            # add a dependency, lockfile and all
uv run main.py             # run inside the project's environment
```

Why manage Python *through* uv instead of the system Python?

- macOS ships an old Python meant for the OS — don't touch it.
- Linux ties Python to system packages; upgrading can break things.
- Windows has no Python by default.

uv gives every club member the **same** interpreter, isolated and reproducible.

## Try it

!!! example "Übung"
    1. `uv init grimm-first && cd grimm-first`
    2. `uv run main.py`
    3. `uv add rich`, then in `main.py`: `from rich import print` and print
       something colourful.

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
