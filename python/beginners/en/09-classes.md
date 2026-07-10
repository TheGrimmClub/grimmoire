# 09 · Classes

> A blueprint for making your own kinds of things — like the club's `Actor`.

## What you'll learn

- What a **class** and an **object** are
- `__init__`, and what `self` means
- Adding **methods** (functions that belong to an object)
- `__str__` — deciding what `print(object)` shows

## The idea

A **class** is a blueprint. Each object you make from it is an **instance**.
This is exactly the day-two package
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero):

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name          # remember the name on this actor

    def name(self):
        return self._name          # a method: called as me.name()

    def enter_dungeon(self):
        print(f"{self._name} betritt das Verlies. 🕯️")

    def __str__(self):
        return f"🧍 {self._name} wartet vor dem Verlies."
```

```python
me = Actor(name="avatar-name")
print(f"Hello {me.name()}")
me.enter_dungeon()
```

- `__init__` runs when you write `Actor(...)`; it sets the object up.
- `self` is *this* object — the one the method is working on.
- `__str__` controls `print(me)`.

## Try it

!!! example "Übung"
    Add a `leave_dungeon()` method and a `location()` method that returns where
    the actor is. Make `__str__` change after entering.

!!! tip "The real thing"
    `grimm.Dungeon().enter()` launches the actual
    [GrimmDungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono) — a
    class that opens a door to a whole program.

---

**Next:** [10 · Tooling · uv](10-tooling-uv.md).
