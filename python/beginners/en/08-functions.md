# 08 · Functions

> Give a name to a piece of work, then reuse it as often as you like.

## What you'll learn

- Defining a function with `def`
- **Parameters** and **arguments**
- Returning a value with `return`
- Default values

## The idea

A **function** bundles steps under a name so you can call it again and again
(you've been calling `print` all along).

```python
def greet(name):
    return f"Hallo {name}!"

print(greet("Hänsel"))    # Hallo Hänsel!
print(greet("Gretel"))    # Hallo Gretel!
```

- `name` is a **parameter** — a placeholder.
- `"Hänsel"` is the **argument** — the real value you pass.
- `return` hands a value back to whoever called the function.

Give defaults so an argument becomes optional:

```python
def brew(strength=1):
    return "🧪" * strength

print(brew())     # 🧪
print(brew(3))    # 🧪🧪🧪
```

!!! tip "Print vs return"
    `print` *shows* a value on screen. `return` *gives it back* so more code can
    use it. Functions almost always want `return`.

## Try it

!!! example "Übung"
    Write `damage(hp, hit=10)` that returns the new hp after a hit. Call it a few
    times, feeding the result back in: `hp = damage(hp)`.

---

**Next:** [09 · Classes](09-classes.md) — your own blueprints.
