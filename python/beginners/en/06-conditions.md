# 06 · Conditions

> Forks in the path: doing different things depending on what's true.

Stories are full of choices — which door, which road, fight or flee. Code makes
choices with **conditions**: it asks a yes/no question and runs different lines
depending on the answer.

## What you'll learn

- `if`, `elif`, `else`
- Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Combining tests with `and`, `or`, `not`
- Why indentation decides what belongs to the `if`

## if / elif / else

A **condition** is an expression that is `True` or `False`. `if` runs its block
only when the condition is `True`:

```python
hp = 30

if hp <= 0:
    print("Du bist gefallen.")
elif hp < 50:
    print("Vorsicht — wenig Leben!")
else:
    print("Dir geht es gut.")
```

Python checks top to bottom and runs the **first** matching block, then skips the
rest. `elif` ("else if") adds more cases; `else` catches everything left.

## Comparisons

These questions give back `True` or `False`:

```python
print(hp == 30)   # True   — equal? (two = signs!)
print(hp != 0)    # True   — not equal
print(hp < 50)    # True   — less than
```

!!! warning "== vs ="
    `=` **assigns** (`hp = 30`). `==` **compares** (`hp == 30`). Using `=` where
    you meant `==` is the classic beginner bug.

## Indentation

The **indentation** (spaces at the start of a line) is how Python knows which
lines belong to the `if`. Same indent = same block:

```python
if has_key:
    print("Du schließt auf.")   # runs only if has_key
    print("Die Tür öffnet sich.")
print("Du gehst weiter.")       # always runs — not indented
```

## Combining conditions

```python
has_key = True
at_door = True

if has_key and at_door:      # both must be True
    print("Die Tür öffnet sich. 🔑")

if tired or hurt:            # at least one True
    print("Du rastest.")

if not alive:                # flips True/False
    print("Game over.")
```

## Try it

!!! example "Übung — which way?"
    Ask the player for a direction with `input(...)`. If they type `"nord"`, print
    a treasure message; otherwise print `"Eine Wand versperrt den Weg."`

??? tip "Solution"
    ```python
    --8<-- "snippets/06-direction.py"
    ```

## Recap

- `if` / `elif` / `else` pick a block by what's `True`; the first match wins.
- Compare with `==`, `!=`, `<`, `>`, `<=`, `>=` — not `=`.
- **Indentation** decides what belongs to the `if`.
- Combine with `and`, `or`, `not`.

## Cheat sheet

| Operator | Means |
|----------|-------|
| `==` / `!=` | equal / not equal |
| `<` `>` `<=` `>=` | compare sizes |
| `and` | both must be true |
| `or` | at least one true |
| `not` | flips true/false |

---

**Next:** [07 · Loops & Controls](07-loops-and-loop-controls.md).
