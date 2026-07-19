# Setup 1 · Install uv

> Before the first spell, the wand: getting `uv` onto your machine.

Every apprentice needs a workbench before they need a spell book. This short
setup chapter gets your machine ready — one tool, then Python itself, then a
test that proves it all works.

You only do this once. If you were at day one and worked through
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup), this is already done
and you can skip ahead to [01 · Commands & Calls](01-commands-and-calls.md).

## What you'll learn

- What **uv** is, in one sentence
- How to install it on macOS, Linux or Windows
- How to check the install worked
- What to do when the shell says `command not found`

## What uv is

`uv` is a single, very fast tool that manages Python for you — the interpreter,
the libraries, and your projects. It replaces the older tangle of `pip`, `venv`
and `pyenv`.

For now, that one sentence is enough. You'll meet what it can really do in
[10 · Tooling · uv](10-tooling-uv.md); here we just need it installed.

## Installing it

Open your shell and run the line for your system.

=== "macOS"

    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Linux"

    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows (PowerShell)"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

!!! note "Reading a command before you run it"
    Piping a script from the internet into your shell is normal for developer
    tools, but it is worth knowing what you just did: it downloaded Astral's
    installer and ran it. You can read it first by opening
    [astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) in a browser.
    A good apprentice looks in the cauldron before drinking.

## Checking it worked

Close your shell and open a **new** one — installers change your `PATH`, and an
old shell won't have noticed.

```sh
uv --version
```

```
uv 0.9.29
```

Your number will differ, and that's fine. Any answer at all means uv is there.

!!! tip "`command not found: uv`"
    The install worked but your shell can't see it yet. In order:

    1. Open a brand-new shell window — the usual fix.
    2. Restart your terminal application entirely.
    3. Still nothing? The installer printed a line telling you which file to add
       to your `PATH`. Scroll back and read it — the answer is in the output.

## Recap

- **uv** is the one tool that manages Python, packages and projects.
- Install it with a single command, then open a **new** shell.
- `uv --version` answering anything means you're ready.

## Cheat sheet

| You want to… | Command |
|--------------|---------|
| Install uv (macOS/Linux) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Install uv (Windows) | `irm https://astral.sh/uv/install.ps1 \| iex` |
| Check uv is there | `uv --version` |

---

**Next:** [Setup 2 · Install Python](a__02-setup-python.md) — the language itself.
