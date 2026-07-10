# 05 · Debugger

> When code misbehaves, stop guessing — look inside it while it runs.

## What you'll learn

- Debugging with `print(...)` (simple and honest)
- Pausing a program with `breakpoint()`
- The core `pdb` moves: step, continue, inspect

## The idea

Code rarely works the first time. That's normal (see the
[Manifest](00-manifest.md)). Debugging is how you *see* what's happening.

The simplest tool is `print`:

```python
total = 0
for coin in [1, 5, 10]:
    total = total + coin
    print("total is now", total)   # watch it grow
```

The real tool is the **debugger**. Drop `breakpoint()` into your code and Python
stops there and hands you a prompt:

```python
def brew(a, b):
    breakpoint()      # execution pauses here
    return a + b
```

At the `(Pdb)` prompt:

| Type | Does |
|------|------|
| `p total` | **p**rint a variable |
| `n` | **n**ext line |
| `s` | **s**tep into a function |
| `c` | **c**ontinue running |
| `q` | **q**uit |

## Try it

!!! example "Übung"
    Take a loop that adds numbers wrong on purpose, add a `breakpoint()`, and
    use `p` and `n` to find the exact line where the total goes astray.

!!! note "Editor & IDE"
    Editors like VS Code have a visual debugger — same ideas, buttons instead of
    letters. Learn the letters first; they work everywhere, even over SSH.

---

**Next:** [06 · Conditions](06-conditions.md) — making choices.
