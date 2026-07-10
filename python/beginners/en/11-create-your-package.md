# 11 · Create Your Package

> Ship something real: turn your code into a package others can install.

## What you'll learn

- The shape of a Python package (`pyproject.toml` + a source folder)
- How `from yourpackage import Thing` works
- Adding tests
- What "publishing" means

## The idea

A **package** is a folder of modules plus a `pyproject.toml` that describes it.
You've already seen one:
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

```
grimm-first/
├── pyproject.toml      # name, version, Python needed, dependencies
├── grimm/              # the package (importable as `grimm`)
│   ├── __init__.py     # re-exports: from grimm import Actor
│   └── actor.py        # your code
└── tests/
    └── test_actor.py   # proof it works
```

A minimal `pyproject.toml`:

```toml
[project]
name = "grimm-first"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Then:

```sh
uv run python -c "from grimm import Actor; print(Actor())"
uv run --with pytest pytest      # run your tests
uv build                          # make a wheel you could publish
```

## Try it

!!! example "Übung"
    Start from `grimm__python__zero`, add a new method to `Actor`, write a test
    for it in `tests/`, and make `task test` pass.

!!! tip "Publishing"
    Packages live on [PyPI](https://pypi.org) so anyone can `pip install` them.
    `uv build` makes the file; `uv publish` uploads it. Ask a mentor before your
    first real publish.

---

You reached the end of the beginner path. Now go
[enter the dungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono). 🕯️
