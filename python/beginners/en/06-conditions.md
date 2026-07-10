# 06 · Conditions

> Forks in the path: doing different things depending on what's true.

## What you'll learn

- `if`, `elif`, `else`
- Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Combining tests with `and`, `or`, `not`
- Why indentation matters in Python

## The idea

A **condition** is a question with a yes/no answer. `if` runs a block only when
the answer is `True`:

```python
hp = 30

if hp <= 0:
    print("Du bist gefallen.")
elif hp < 50:
    print("Vorsicht — wenig Leben!")
else:
    print("Dir geht es gut.")
```

The **indentation** (the spaces at the start of a line) is how Python knows
which lines belong to the `if`. Same indent = same block.

Combine questions:

```python
has_key = True
at_door = True

if has_key and at_door:
    print("Die Tür öffnet sich. 🔑")
```

## Try it

!!! example "Übung"
    Ask for a direction (`"nord"`, `"süd"`, …). If it's `"nord"`, print a
    treasure message; for anything else, print "Eine Wand versperrt den Weg."

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
