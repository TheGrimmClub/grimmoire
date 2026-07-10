# 09 · Klassen

> Ein Bauplan, um deine eigenen Arten von Dingen zu erschaffen — wie den `Actor` des Clubs.

## Was du lernst

- Was eine **Klasse** und ein **Objekt** sind
- `__init__` und was `self` bedeutet
- **Methoden** hinzufügen (Funktionen, die zu einem Objekt gehören)
- `__str__` — festlegen, was `print(objekt)` zeigt

## Die Idee

Eine **Klasse** ist ein Bauplan. Jedes Objekt, das du daraus machst, ist eine
**Instanz**. Genau das ist das Tag-zwei-Paket
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero):

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name          # den Namen auf diesem Actor merken

    def name(self):
        return self._name          # eine Methode: aufgerufen als me.name()

    def enter_dungeon(self):
        print(f"{self._name} betritt das Verlies. 🕯️")

    def __str__(self):
        return f"🧍 {self._name} wartet vor dem Verlies."
```

```python
me = Actor(name="avatar-name")
print(f"Hallo {me.name()}")
me.enter_dungeon()
```

- `__init__` läuft, wenn du `Actor(...)` schreibst; es richtet das Objekt ein.
- `self` ist *dieses* Objekt — das, an dem die Methode arbeitet.
- `__str__` steuert `print(me)`.

## Probier es

!!! example "Übung"
    Füge eine Methode `leave_dungeon()` und eine Methode `location()` hinzu, die
    zurückgibt, wo der Actor ist. Lass `__str__` sich ändern, nachdem er das
    Verlies betreten hat.

!!! tip "Die echte Sache"
    `grimm.Dungeon().enter()` startet den echten
    [GrimmDungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono) — eine
    Klasse, die eine Tür zu einem ganzen Programm öffnet.

---

**Weiter:** [10 · Werkzeug · uv](10-tooling-uv.md).
