# 09 · Classes

> A blueprint for making your own kinds of things — like the club's `Actor`.

You've used other people's objects all along: strings, lists, `print`. Now you
build your own. A **class** lets you invent a new *kind* of thing, decide what it
remembers, and what it can do. This is the heart of the day-two package,
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

## What you'll learn

- What a **class** and an **object** (instance) are
- `__init__`, and what `self` really means
- Adding **methods** — functions that belong to an object
- `__str__` — deciding what `print(object)` shows
- The difference between a method and a plain function

## Blueprint vs. thing

A **class** is a blueprint. An **object** is a real thing built from it. One
blueprint, many objects:

```python
class Actor:
    pass          # an empty blueprint for now

a = Actor()       # one object
b = Actor()       # a different object
print(a is b)     # False — two separate things
```

`Actor()` (with brackets — remember [chapter 01](01-commands-and-calls.md)!)
**builds** a new actor. `a` and `b` are two independent actors.

## `__init__`: setting an object up

Most things need to start with some state. The `__init__` method runs
**automatically** the moment you write `Actor(...)`:

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name        # remember the name on THIS actor
```

- `name="Namenloser"` is a **default** (see [chapter 08](08-functions.md)) — so
  `Actor()` still works, giving a nameless hero.
- `self._name = name` stores the name **on the object** so it survives after
  `__init__` finishes.

!!! note "What is `self`?"
    `self` is *this particular object* — the one being built or worked on. Python
    passes it in for you. When you write `Actor(name="Hans")`, inside `__init__`
    `self` **is** that new actor, and `self._name = "Hans"` writes onto it. Every
    method's first parameter is `self`.

## Methods: what an object can do

A **method** is a function that lives inside a class. It always takes `self`
first, so it can reach the object's own data:

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name

    def name(self):
        return self._name                 # read this actor's name

    def enter_dungeon(self):
        print(f"{self._name} betritt das Verlies. 🕯️")
```

You call a method **on** an object with a dot:

```python
me = Actor(name="avatar-name")
print(f"Hello {me.name()}")   # Hello avatar-name
me.enter_dungeon()            # avatar-name betritt das Verlies. 🕯️
```

!!! tip "Method vs. function"
    `len(x)` is a **function** — it stands alone. `me.name()` is a **method** — it
    belongs to `me` and already knows *which* actor it's about. The dot is the
    difference.

## `__str__`: a friendly face

Print an object without `__str__` and you get something ugly like
`<grimm.actor.Actor object at 0x104f…>`. Define `__str__` to choose what
`print` shows:

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name
        self._in_dungeon = False

    def enter_dungeon(self):
        self._in_dungeon = True
        print(f"{self._name} betritt das Verlies. 🕯️")

    def __str__(self):
        ort = "im Verlies" if self._in_dungeon else "vor dem Verlies"
        return f"🧍 {self._name} wartet {ort}."
```

```python
me = Actor(name="Hans")
print(me)              # 🧍 Hans wartet vor dem Verlies.
me.enter_dungeon()
print(me)              # 🧍 Hans wartet im Verlies.   ← it changed!
```

The object *remembers* (`self._in_dungeon`), so its printed form changes over
time. That's state.

## A common mistake

!!! warning "Don't forget `self`"
    Every method needs `self` as its first parameter, and every access to the
    object's own data goes through `self`:

    ```python
    def name(self):
        return _name        # NameError: '_name' is not defined
    ```
    ```python
    def name(self):
        return self._name   # ✓ correct
    ```

## Try it

!!! example "Übung 1 — leave the dungeon"
    Add a `leave_dungeon()` method that sets `self._in_dungeon = False` and prints
    a line. Check that `print(me)` changes back.

!!! example "Übung 2 — a location"
    Add a `location()` method that returns `"im Verlies"` or `"vor dem Verlies"`.
    Reuse it inside `__str__` so the text lives in one place.

??? tip "Solution for Übung 2"
    ```python
    --8<-- "snippets/09-location.py"
    ```

!!! tip "The real thing"
    `grimm.Dungeon().enter()` is itself a class — one that opens a door to the
    whole [GrimmDungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono)
    program. Classes scale from a toy `Actor` to a real adventure.

## Recap

- A **class** is a blueprint; each `Actor()` is an **object**.
- `__init__` sets an object up; `self` is *this* object.
- **Methods** are functions on an object, always taking `self` first.
- `__str__` controls `print(object)`; objects can **remember** state.

## Cheat sheet

| Piece | Means |
|-------|-------|
| `class Actor:` | define a blueprint |
| `def __init__(self, ...)` | set up a new object |
| `self._name = name` | store data on the object |
| `def enter_dungeon(self):` | a method (action) |
| `me.enter_dungeon()` | call a method on an object |
| `def __str__(self):` | what `print(me)` shows |

---

**Next:** [10 · Tooling · uv](10-tooling-uv.md).
