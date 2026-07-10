# 04 · Variables & Values

> Giving names to things so your program can remember them.

A program that can't remember anything can't do much. **Variables** are how Python
holds on to a value — a name, a number, a whole list — so you can use it later.

## What you'll learn

- What a **variable** is (a name pointing at a value)
- The everyday **types**: `int`, `float`, `str`, `bool`
- Collections: `list` and `dict`
- How to inspect a value with `type(...)`

## Names and values

A **variable** is a label you stick on a value with `=`:

```python
name = "avatar-name"   # str  (text)
hp = 100               # int  (whole number)
speed = 3.5            # float (decimal)
alive = True           # bool  (True / False)
```

The name goes on the left, the value on the right. Later, the name *stands for*
the value:

```python
print(hp)          # 100
hp = hp - 10       # read the old value, store a new one
print(hp)          # 90
```

!!! note "= is not equals"
    In maths `=` means "is equal to". In Python `=` means **"put this value into
    this name"**. To *compare*, you use `==` (next chapter).

## Types

Every value has a **type**. `type(...)` tells you which:

```python
print(type(hp))       # <class 'int'>
print(type(name))     # <class 'str'>
```

| Type | Example | Is |
|------|---------|----|
| `int` | `42` | whole number |
| `float` | `3.14` | decimal |
| `str` | `"Grimm"` | text |
| `bool` | `True` | yes/no |

Type matters: `"5" + "5"` is `"55"` (text joined), but `5 + 5` is `10` (numbers
added). Mixing them is an error — `"5" + 5` raises `TypeError`.

## Collections

When you need *many* values, reach for a **list** (ordered) or a **dict**
(labelled):

```python
inventory = ["Schwert", "Brot", "Schlüssel"]   # list
hero = {"name": "Hans", "hp": 100}              # dict

print(inventory[0])    # Schwert   — lists count from 0
print(hero["hp"])      # 100       — dicts look up by key

inventory.append("Fackel")   # add to the list
```

## Try it

!!! example "Übung — a hero sheet"
    Make variables for a hero: `name`, `hp` (an int), and an `inventory` list.
    Print one sentence with an f-string:
    `f"{name} hat {hp} HP und trägt {inventory}."`

??? tip "Solution"
    ```python
    --8<-- "snippets/04-hero.py"
    ```

## Recap

- A **variable** is a name pointing at a value; `=` assigns, `==` compares.
- Values have **types**: `int`, `float`, `str`, `bool`.
- **Lists** are ordered (`inventory[0]`), **dicts** look up by key (`hero["hp"]`).
- `type(x)` tells you the type.

## Cheat sheet

| Piece | Means |
|-------|-------|
| `x = 5` | put `5` into the name `x` |
| `type(x)` | the type of `x` |
| `[1, 2, 3]` | a list (ordered) |
| `{"k": "v"}` | a dict (key→value) |
| `lst[0]` / `d["k"]` | read by index / key |

---

**Next:** [05 · Debugger](05-debugger.md) — seeing what your code really does.
