# 07 · Loops & Controls

> Doing something again — and knowing when to stop.

## What you'll learn

- `for` loops over a collection
- `while` loops until a condition changes
- `range(...)` for counting
- `break` and `continue` to steer a loop

## The idea

A **loop** repeats a block. A `for` loop walks through a collection:

```python
for item in ["Schwert", "Brot", "Schlüssel"]:
    print("Du trägst:", item)
```

Count with `range`:

```python
for i in range(3):        # 0, 1, 2
    print("Schritt", i)
```

A `while` loop runs until its condition becomes `False`:

```python
torches = 3
while torches > 0:
    print("Eine Fackel brennt.")
    torches = torches - 1
```

Steer from inside:

```python
for door in doors:
    if door == "verschlossen":
        continue       # skip this one, go to the next
    if door == "Ausgang":
        break          # leave the loop entirely
```

!!! warning "Endlosschleife"
    A `while` whose condition never becomes `False` runs forever. Make sure
    something inside changes. `Ctrl+C` stops a runaway program.

## Try it

!!! example "Übung"
    Loop over `range(1, 11)` and print only the even numbers (hint: `% 2 == 0`).

---

**Next:** [08 · Functions](08-functions.md) — naming a piece of work.
