# 05 · Debugger

> When code misbehaves, stop guessing — look inside it while it runs.

Code rarely works the first time. That's normal — the [Manifesto](00-manifest.md)
says so. Being stuck isn't failure; it's a point on the map. Debugging is how you
*see* what your code is actually doing, instead of guessing.

## What you'll learn

- Debugging with `print(...)` — simple and honest
- Pausing a program with `breakpoint()`
- The core `pdb` moves: print, next, step, continue
- How to read an error message

## Reading an error

When Python stops with an error, read it **from the bottom up**:

```
Traceback (most recent call last):
  File "spell.py", line 3, in <module>
    print(hp + name)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

The last line is *what* went wrong (`TypeError`, adding an int and a str). The
`File ... line 3` is *where*. Most fixes start by reading that bottom line
carefully.

## Print debugging

The simplest tool is `print` — sprinkle it in to watch values change:

```python
total = 0
for coin in [1, 5, 10]:
    total = total + coin
    print("total is now", total)   # 1, then 6, then 16
```

Honest, quick, works everywhere. Just remember to remove them afterwards.

## The real debugger

`breakpoint()` **pauses** your program and drops you into an interactive prompt,
right in the middle of the run:

```python
def brew(a, b):
    breakpoint()      # execution stops here
    return a + b
```

At the `(Pdb)` prompt you steer:

| Type | Does |
|------|------|
| `p total` | **p**rint a variable's value |
| `n` | **n**ext line |
| `s` | **s**tep into a function call |
| `c` | **c**ontinue running |
| `q` | **q**uit |

You get to *look around* while the program is frozen — inspect any variable,
step forward one line at a time, and watch exactly where things go wrong.

## Try it

!!! example "Übung — catch it in the act"
    Take the coin loop below, drop a `breakpoint()` inside it, and use `p total`
    and `n` to watch the total grow one coin at a time.

??? tip "Solution"
    ```python
    --8<-- "snippets/05-fix.py"
    ```

!!! note "Editor & IDE"
    Editors like VS Code have a visual debugger — same ideas, buttons instead of
    letters. Learn the letters first; they work everywhere, even over SSH.

## Recap

- Read tracebacks **bottom-up**: the last line says what and where.
- `print(...)` is quick, honest debugging.
- `breakpoint()` pauses the program; `p`, `n`, `s`, `c`, `q` steer it.

## Cheat sheet

| Piece | Does |
|-------|------|
| `breakpoint()` | pause and open the debugger |
| `p x` | print variable `x` |
| `n` / `s` | next line / step into |
| `c` / `q` | continue / quit |

---

**Next:** [06 · Conditions](06-conditions.md) — making choices.
