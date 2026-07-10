# 02 · Imports

> Standing on the shoulders of giants: using code from other files and libraries.

You almost never start from nothing. Python comes with a huge **standard library**,
and the world has written millions more packages. **Importing** is how you reach
for that work instead of rewriting it.

## What you'll learn

- What a **module** and a **package** are
- `import x` vs. `from x import y`
- How renaming with `as` helps
- Where Python looks for things to import
- The famous easter egg, `import antigravity`

## Module and package

A **module** is a single `.py` file full of code. A **package** is a folder of
modules that belong together. Either way, you reach inside with `import`.

```python
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
```

`import math` brings in the whole module; you then reach its contents with a dot:
`math.sqrt`, `math.pi`.

## `from ... import ...`

If you only need one or two things, import them by name and skip the prefix:

```python
from math import sqrt, pi
print(sqrt(16))    # no "math." needed
print(pi)
```

The club's own package works the same way:

```python
from grimm import Actor
me = Actor()
print(me)
```

## Renaming with `as`

Sometimes a name is long, or clashes with your own. `as` gives it a nickname:

```python
import statistics as stats
print(stats.mean([1, 2, 3]))   # 2

from grimm import Actor as Hero
me = Hero(name="Hans")
```

## Where imports come from

`import x` finds `x` if it's part of Python's standard library, installed in your
environment (via `uv add`), or a file next to your program. That's why
`from grimm import Actor` works once you're inside the `grimm__python__zero`
project — the `grimm/` folder sits right there.

!!! warning "Don't shadow the standard library"
    If you name your own file `math.py` or `random.py`, `import math` may find
    *your* file instead of Python's and behave strangely. Avoid naming files after
    modules you import.

!!! tip "Try the easter egg"
    Type `import antigravity` in a Python shell. Python was making jokes before
    you were born. (`grimm.Dungeon` — [chapter 09](09-classes.md) — plays with the
    same idea.)

## Try it

!!! example "Übung 1 — random direction"
    `import random`, then print `random.choice(["Nord", "Süd", "Ost", "West"])`.
    Run it a few times.

!!! example "Übung 2 — your package"
    Clone [grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero),
    then in a REPL run `from grimm import Actor` and make one.

??? tip "Solution for Übung 1"
    <!-- snippet: 02-random-direction.py -->
    ```python
    import random

    print("Du gehst nach", random.choice(["Nord", "Süd", "Ost", "West"]))
    ```
    <!-- endsnippet -->

## Recap

- A **module** is a file; a **package** is a folder of modules.
- `import x` brings the whole thing (`x.thing`); `from x import y` brings one name.
- `as` renames an import.
- Don't name your files after modules you import.

## Cheat sheet

| Form | Meaning |
|------|---------|
| `import math` | whole module; use `math.sqrt` |
| `from math import sqrt` | just `sqrt` |
| `import numpy as np` | rename to `np` |
| `from grimm import Actor` | one name from a package |

---

**Next:** [03 · argparse](03-argparse.md) — reading input from the command line.
