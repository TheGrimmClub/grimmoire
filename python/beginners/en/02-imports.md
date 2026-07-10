# 02 · Imports

> Standing on the shoulders of giants: using code from other files and libraries.

## What you'll learn

- What a **module** and a **package** are
- `import x` vs `from x import y`
- Where Python looks for things to import
- The famous easter egg: `import antigravity`

## The idea

You almost never start from nothing. **Importing** pulls in code someone else
(or you, earlier) already wrote.

```python
import math
print(math.sqrt(16))      # 4.0

from math import sqrt
print(sqrt(16))           # same thing, shorter
```

A **module** is one `.py` file. A **package** is a folder of modules. The club's
own package is `grimm`:

```python
from grimm import Actor
me = Actor()
print(me)
```

!!! tip "Try the easter egg"
    Type `import antigravity` in a Python shell. Python was making jokes before
    you were born.

## Try it

!!! example "Übung"
    1. `import random` and print `random.choice(["Nord", "Süd", "Ost", "West"])`.
    2. Clone [grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero)
       and run `from grimm import Actor`.

## Cheat sheet

| Form | Meaning |
|------|---------|
| `import math` | bring in the whole module; use `math.sqrt` |
| `from math import sqrt` | bring in just `sqrt` |
| `import math as m` | rename it to `m` |
| `from grimm import Actor` | one name from a package |

---

**Next:** [03 · argparse](03-argparse.md) — reading input from the command line.
