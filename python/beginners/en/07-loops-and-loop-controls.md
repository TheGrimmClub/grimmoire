# 07 · Loops & Controls

> Doing something again — and knowing when to stop.

Computers are brilliant at repetition. A **loop** runs the same block many times,
so you write it once instead of copying it a hundred times.

## What you'll learn

- `for` loops over a collection
- `while` loops until a condition changes
- `range(...)` for counting
- `break` and `continue` to steer a loop

## for: walk through a collection

A `for` loop takes each item of a collection in turn:

```python
for item in ["Schwert", "Brot", "Schlüssel"]:
    print("Du trägst:", item)
```

The indented body runs once per item, with `item` set to each value.

## range: counting

`range` makes a sequence of numbers — handy for repeating a fixed number of
times:

```python
for i in range(3):        # 0, 1, 2
    print("Schritt", i)

for i in range(1, 4):     # 1, 2, 3  (start, stop)
    print(i)
```

`range(n)` stops *before* `n`, so `range(3)` gives `0, 1, 2` — three values.

## while: until a condition changes

A `while` loop repeats **as long as** its condition is `True`:

```python
torches = 3
while torches > 0:
    print("Eine Fackel brennt.")
    torches = torches - 1     # move toward the end!
```

!!! warning "Endless loop"
    If the condition never becomes `False`, the loop runs forever. Make sure
    something inside changes it. `Ctrl+C` stops a runaway program.

## break and continue

Steer a loop from the inside:

```python
for door in doors:
    if door == "verschlossen":
        continue       # skip this one, go to the next
    if door == "Ausgang":
        break          # leave the loop entirely
    print("Du öffnest:", door)
```

- `continue` — skip the rest of *this* turn, move to the next.
- `break` — stop the whole loop now.

## Try it

!!! example "Übung — only the evens"
    Loop over `range(1, 11)` and print only the even numbers. Hint: a number is
    even when `n % 2 == 0` (`%` is the remainder).

??? tip "Solution"
    ```python
    --8<-- "snippets/07-evens.py"
    ```

## Recap

- `for` walks a collection; `while` repeats until a condition flips.
- `range(n)` counts `0 … n-1`; `range(a, b)` counts `a … b-1`.
- `continue` skips a turn; `break` ends the loop.
- Always make a `while` able to end.

## Cheat sheet

| Piece | Does |
|-------|------|
| `for x in seq:` | run once per item |
| `range(n)` | `0 … n-1` |
| `while cond:` | repeat while `cond` is true |
| `continue` / `break` | skip a turn / end the loop |

---

**Next:** [08 · Functions](08-functions.md) — naming a piece of work.
