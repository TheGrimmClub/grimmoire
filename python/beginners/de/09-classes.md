# 09 · Klassen

> Ein Bauplan, um deine eigenen Arten von Dingen zu erschaffen — wie den `Actor` des Clubs.

Du hast die ganze Zeit die Objekte anderer benutzt: Strings, Listen, `print`.
Jetzt baust du deine eigenen. Eine **Klasse** lässt dich eine neue *Art* von Ding
erfinden, festlegen, was es sich merkt, und was es tun kann. Das ist das Herz des
Tag-zwei-Pakets
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

## Was du lernst

- Was eine **Klasse** und ein **Objekt** (eine Instanz) sind
- `__init__` und was `self` wirklich bedeutet
- **Methoden** hinzufügen — Funktionen, die zu einem Objekt gehören
- `__str__` — festlegen, was `print(objekt)` zeigt
- Der Unterschied zwischen einer Methode und einer normalen Funktion

## Bauplan vs. Ding

Eine **Klasse** ist ein Bauplan. Ein **Objekt** ist ein echtes Ding, das daraus
gebaut wird. Ein Bauplan, viele Objekte:

```python
class Actor:
    pass          # vorerst ein leerer Bauplan

a = Actor()       # ein Objekt
b = Actor()       # ein anderes Objekt
print(a is b)     # False — zwei getrennte Dinge
```

`Actor()` (mit Klammern — erinnere dich an [Kapitel 01](01-commands-and-calls.md)!)
**baut** einen neuen Actor. `a` und `b` sind zwei unabhängige Actors.

## `__init__`: ein Objekt einrichten

Die meisten Dinge müssen mit etwas Zustand starten. Die Methode `__init__` läuft
**automatisch** in dem Moment, in dem du `Actor(...)` schreibst:

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name        # den Namen auf DIESEM Actor merken
```

- `name="Namenloser"` ist ein **Standardwert** (siehe
  [Kapitel 08](08-functions.md)) — so funktioniert `Actor()` weiterhin und ergibt
  einen namenlosen Helden.
- `self._name = name` speichert den Namen **auf dem Objekt**, damit er überlebt,
  nachdem `__init__` fertig ist.

!!! note "Was ist `self`?"
    `self` ist *dieses bestimmte Objekt* — das, das gerade gebaut oder bearbeitet
    wird. Python übergibt es für dich. Wenn du `Actor(name="Hans")` schreibst, *ist*
    `self` innerhalb von `__init__` genau dieser neue Actor, und
    `self._name = "Hans"` schreibt darauf. Der erste Parameter jeder Methode ist
    `self`.

## Methoden: was ein Objekt tun kann

Eine **Methode** ist eine Funktion, die in einer Klasse lebt. Sie nimmt immer
zuerst `self`, damit sie an die eigenen Daten des Objekts kommt:

```python
class Actor:
    def __init__(self, name="Namenloser"):
        self._name = name

    def name(self):
        return self._name                 # den Namen dieses Actors lesen

    def enter_dungeon(self):
        print(f"{self._name} betritt das Verlies. 🕯️")
```

Du rufst eine Methode **auf** einem Objekt mit einem Punkt auf:

```python
me = Actor(name="avatar-name")
print(f"Hallo {me.name()}")   # Hallo avatar-name
me.enter_dungeon()            # avatar-name betritt das Verlies. 🕯️
```

!!! tip "Methode vs. Funktion"
    `len(x)` ist eine **Funktion** — sie steht allein. `me.name()` ist eine
    **Methode** — sie gehört zu `me` und weiß schon, um *welchen* Actor es geht.
    Der Punkt ist der Unterschied.

## `__str__`: ein freundliches Gesicht

Gib ein Objekt ohne `__str__` aus, und du bekommst so etwas Hässliches wie
`<grimm.actor.Actor object at 0x104f…>`. Definiere `__str__`, um zu wählen, was
`print` zeigt:

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
print(me)              # 🧍 Hans wartet im Verlies.   ← es hat sich geändert!
```

Das Objekt *merkt sich* (`self._in_dungeon`), also ändert sich seine
Druckform mit der Zeit. Das ist Zustand.

## Ein häufiger Fehler

!!! warning "Vergiss `self` nicht"
    Jede Methode braucht `self` als ersten Parameter, und jeder Zugriff auf die
    eigenen Daten des Objekts geht über `self`:

    ```python
    def name(self):
        return _name        # NameError: '_name' is not defined
    ```
    ```python
    def name(self):
        return self._name   # ✓ richtig
    ```

## Probier es

!!! example "Übung 1 — das Verlies verlassen"
    Füge eine Methode `leave_dungeon()` hinzu, die `self._in_dungeon = False`
    setzt und eine Zeile ausgibt. Prüfe, dass sich `print(me)` zurückändert.

!!! example "Übung 2 — ein Ort"
    Füge eine Methode `location()` hinzu, die `"im Verlies"` oder
    `"vor dem Verlies"` zurückgibt. Nutze sie in `__str__` wieder, damit der Text
    an einer Stelle lebt.

??? tip "Lösung für Übung 2"
    ```python
    --8<-- "snippets/09-location.py"
    ```

!!! tip "Die echte Sache"
    `grimm.Dungeon().enter()` ist selbst eine Klasse — eine, die eine Tür zum
    ganzen [GrimmDungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono)-
    Programm öffnet. Klassen skalieren vom Spielzeug-`Actor` bis zum echten
    Abenteuer.

## Zusammenfassung

- Eine **Klasse** ist ein Bauplan; jedes `Actor()` ist ein **Objekt**.
- `__init__` richtet ein Objekt ein; `self` ist *dieses* Objekt.
- **Methoden** sind Funktionen an einem Objekt, die immer zuerst `self` nehmen.
- `__str__` steuert `print(objekt)`; Objekte können Zustand **merken**.

## Spickzettel

| Teil | Bedeutet |
|------|----------|
| `class Actor:` | einen Bauplan definieren |
| `def __init__(self, ...)` | ein neues Objekt einrichten |
| `self._name = name` | Daten auf dem Objekt speichern |
| `def enter_dungeon(self):` | eine Methode (Aktion) |
| `me.enter_dungeon()` | eine Methode auf einem Objekt aufrufen |
| `def __str__(self):` | was `print(me)` zeigt |

---

**Weiter:** [10 · Werkzeug · uv](10-tooling-uv.md).
