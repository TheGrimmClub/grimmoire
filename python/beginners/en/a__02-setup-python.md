# Setup 2 · Install Python

> The language itself — installed by uv, so it belongs to you and not to your operating system.

You have the wand. Now the magic it channels.

Python is a program like any other, and you might already have one on your
machine. We're going to install our own anyway, and this chapter is partly about
*why* that isn't wasteful.

## What you'll learn

- Why the club doesn't use the Python that came with your computer
- Installing Python with one uv command
- Checking which version you got
- Where uv actually put it

## Why not the Python you already have

Type this — it may answer, or it may not:

```sh
uv run python --version
```

Either way, the club installs its own. The reasons differ by system:

- **macOS** ships an old Python that the operating system itself uses. Change it
  and you can break parts of macOS. Leave it alone.
- **Linux** ties Python to system packages, so upgrading Python can uninstall
  things you needed.
- **Windows** usually has no Python at all until you add one.

!!! note "The real reason: everyone the same"
    A shared workbench only works if the tools match. When every apprentice runs
    the same interpreter, "it works on mine" stops being an argument and code
    that runs for you runs for the person next to you.

## Installing it

```sh
uv python install 3.13
```

That downloads Python 3.13 and keeps it in uv's own store — not mixed into your
system.

To see what you have:

```sh
uv python list
```

You'll get a list of versions, with the installed ones marked. Several entries is
normal and nothing to worry about.

## Which Python will run?

```sh
uv run python --version
```

```
Python 3.13.0
```

`uv run` is the important half of that command: it picks the right Python for
where you are, rather than whatever the shell happens to find first. From here
on, the book always runs Python through `uv run` — so you never have to wonder
which interpreter answered.

!!! tip "A different number?"
    Anything `3.13` or newer is fine for this book. If you see `3.9` or similar,
    you're being answered by a system Python — check that
    `uv python install 3.13` finished without an error.

## Recap

- The system Python belongs to your **operating system**; leave it be.
- `uv python install 3.13` gives you one that belongs to **you**.
- `uv run python` always picks the right one.

## Cheat sheet

| You want to… | Command |
|--------------|---------|
| Install Python 3.13 | `uv python install 3.13` |
| See installed versions | `uv python list` |
| Check which one runs | `uv run python --version` |

---

**Next:** [Setup 3 · Test Your Installation](a__03-test-installation.md) — proving it all works.
