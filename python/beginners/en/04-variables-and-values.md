# 04 · Variables & Values

> Giving names to things so your program can remember them.

## What you'll learn

- What a **variable** is (a name pointing at a value)
- The everyday **types**: `int`, `float`, `str`, `bool`
- Collections: `list` and `dict`
- How to inspect a value with `type(...)`

## The idea

A **variable** is a label you stick on a value:

```python
name = "avatar-name"   # str  (text)
health = 100           # int  (whole number)
speed = 3.5            # float (decimal)
alive = True           # bool  (True / False)
```

Values come in **types**. `type(...)` tells you which:

```python
print(type(health))    # <class 'int'>
```

Collections hold many values:

```python
inventory = ["Schwert", "Brot", "Schlüssel"]   # list — ordered
hero = {"name": "Hans", "hp": 100}              # dict — key → value

print(inventory[0])    # Schwert
print(hero["hp"])      # 100
```

## Try it

!!! example "Übung"
    Make variables for a hero: `name`, `hp`, and an `inventory` list. Print a
    sentence with an f-string: `f"{name} hat {hp} HP und trägt {inventory}."`

## Cheat sheet

| Type | Example | Is |
|------|---------|----|
| `int` | `42` | whole number |
| `float` | `3.14` | decimal |
| `str` | `"Grimm"` | text |
| `bool` | `True` | yes/no |
| `list` | `[1, 2, 3]` | ordered collection |
| `dict` | `{"k": "v"}` | key→value map |

---

**Next:** [05 · Debugger](05-debugger.md) — seeing what your code really does.
