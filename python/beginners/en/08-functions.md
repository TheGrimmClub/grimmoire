# 08 · Functions

> Give a name to a piece of work, then reuse it as often as you like.

You've been *calling* functions since [chapter 01](01-commands-and-calls.md) —
`print(...)`. Now you write your own. A function lets you take a few steps, give
them a name, and run them again and again without repeating yourself.

## What you'll learn

- Defining a function with `def`
- **Parameters** vs. **arguments**
- Returning a value with `return`
- Default values, so an argument becomes optional
- Why `return` is not the same as `print`

## Defining and calling

```python
def greet(name):
    return f"Hallo {name}!"

print(greet("Hänsel"))    # Hallo Hänsel!
print(greet("Gretel"))    # Hallo Gretel!
```

- `def` starts the definition.
- `greet` is the **name**.
- `name` is a **parameter** — a placeholder that gets filled in when the function
  is called.
- The indented lines are the **body** — what runs when you call it.

`"Hänsel"` is an **argument**: the real value you pass for `name`. Parameter =
the name in the definition; argument = the value at the call.

## `return`: handing a value back

`return` sends a value back to whoever called the function, and ends it:

```python
def double(x):
    return x * 2

result = double(21)    # result is now 42
print(result)
```

The call `double(21)` *becomes* `42`, so you can store it, print it, or feed it
into another call. A function without `return` gives back `None` (nothing).

!!! warning "return is not print"
    `print` **shows** a value on screen and throws it away. `return` **gives it
    back** so more code can use it.

    ```python
    def add(a, b):
        print(a + b)      # shows it, but you can't reuse it
    total = add(2, 3)     # prints 5, but total is None!
    ```
    ```python
    def add(a, b):
        return a + b      # ✓ hands it back
    total = add(2, 3)     # total is 5
    ```

## Default values

Give a parameter a default and the argument becomes optional (you saw this with
`Actor(name="Namenloser")` in the class chapter):

```python
def brew(strength=1):
    return "🧪" * strength

print(brew())     # 🧪
print(brew(3))    # 🧪🧪🧪
```

## Worked example

A tiny combat step, built from functions:

```python
def damage(hp, hit=10):
    return hp - hit

hp = 100
hp = damage(hp)        # 90
hp = damage(hp, 25)    # 65
print("HP:", hp)
```

Each call takes the current `hp` and gives back a new one — you feed the result
back in. Small functions, combined, become a program.

## Try it

!!! example "Übung 1 — greet loudly"
    Write `shout(text)` that returns `text` in capitals (hint: strings have an
    `.upper()` method). Test it with `print(shout("hallo"))`.

!!! example "Übung 2 — heal"
    Write `heal(hp, amount=20)` that returns the new hp. Chain a few `damage` and
    `heal` calls, feeding the result back each time.

??? tip "Solution for Übung 1"
    <!-- snippet: 08-shout.py -->
    ```python
    def shout(text):
        return text.upper()


    print(shout("hallo"))   # HALLO
    ```
    <!-- endsnippet -->

## Recap

- `def name(parameters):` defines a function; the body is indented.
- **Parameter** = placeholder in the definition; **argument** = value at the call.
- `return` hands a value back (most functions want it); no `return` → `None`.
- **Defaults** make arguments optional.

## Cheat sheet

| Piece | Means |
|-------|-------|
| `def f(x):` | define a function with parameter `x` |
| `return v` | hand back `v` and stop |
| `f(3)` | call `f` with argument `3` |
| `def f(x=1):` | `x` defaults to `1` |

---

**Next:** [09 · Classes](09-classes.md) — your own blueprints.
