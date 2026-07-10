# 11 · Create Your Package

> Ship something real: turn your code into a package others can install.

This is the finish line of the beginner path. Everything so far — calls, imports,
variables, functions, classes, uv — comes together here into a **package**: a
tidy bundle of code that anyone can `pip install` and `import`.

## What you'll learn

- The shape of a Python package (`pyproject.toml` + a source folder)
- How `from yourpackage import Thing` works
- Adding tests
- What "publishing" means

## The shape of a package

A **package** is a folder of modules plus a `pyproject.toml` that describes it.
You've already seen one:
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

```
grimm-first/
├── pyproject.toml      # name, version, Python needed, dependencies
├── grimm/              # the package — importable as `grimm`
│   ├── __init__.py     # re-exports: from grimm import Actor
│   └── actor.py        # your code
└── tests/
    └── test_actor.py   # proof it works
```

The folder `grimm/` **is** the package: its name is the name you `import`. The
`__init__.py` file is what makes it a package, and it's where you choose what to
re-export.

## `pyproject.toml`

This one file describes your project to Python and to the world:

```toml
[project]
name = "grimm-first"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- `name` is the **distribution** name (what people `pip install`).
- `version` — bump it every time you publish.
- `dependencies` — other packages yours needs (uv fills these when you `uv add`).

!!! note "Import name vs. install name"
    They can differ! `grimm__python__zero` installs as `pip install
    grimm-python-zero` but you write `from grimm import Actor`. The **folder**
    decides the import name; `pyproject.toml`'s `name` decides the install name.

## Make it, test it, build it

```sh
uv run python -c "from grimm import Actor; print(Actor())"
uv run --with pytest pytest      # run your tests
uv build                          # make an installable wheel in dist/
```

A **test** is code that checks your code. It doubles as a promise: "this still
works." Keeping tests green as you change things is how real projects stay
trustworthy.

```python
# tests/test_actor.py
from grimm import Actor

def test_default_name():
    assert Actor().name() == "Namenloser"
```

## Publishing

Packages live on [PyPI](https://pypi.org), the Python Package Index, so anyone
can install them:

```sh
uv build       # makes the files in dist/
uv publish     # uploads them to PyPI
```

After that, the whole world can `pip install your-package`. `grimm-python-zero`
itself is published exactly this way — via an automated release on GitHub.

!!! warning "Publishing is forever"
    A version on PyPI can't be re-uploaded or truly deleted. Get it working
    locally first, and ask a mentor before your first real publish.

## Try it

!!! example "Übung — extend and prove it"
    Start from `grimm__python__zero`. Add a new method to `Actor` (e.g.
    `leave_dungeon()`), write a test for it in `tests/`, and make `task test`
    pass.

??? tip "A starting test"
    ```python
    --8<-- "snippets/11-test-leave.py"
    ```

## Recap

- A **package** = a source folder + `pyproject.toml`.
- `__init__.py` makes the folder a package and chooses the exports.
- Install name (`pyproject`) and import name (folder) can differ.
- `uv build` makes it; `uv publish` shares it on PyPI — permanently.

---

You reached the end of the beginner path. Now go
[enter the dungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono). 🕯️
