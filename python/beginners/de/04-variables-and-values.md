# 04 · Variablen & Werte

> Dingen Namen geben, damit dein Programm sie sich merken kann.

Ein Programm, das sich nichts merken kann, kann nicht viel. **Variablen** sind,
wie Python einen Wert festhält — einen Namen, eine Zahl, eine ganze Liste —,
damit du ihn später nutzen kannst.

## Was du lernst

- Was eine **Variable** ist (ein Name, der auf einen Wert zeigt)
- Die alltäglichen **Typen**: `int`, `float`, `str`, `bool`
- Sammlungen: `list` und `dict`
- Wie man einen Wert mit `type(...)` untersucht

## Namen und Werte

Eine **Variable** ist ein Etikett, das du mit `=` auf einen Wert klebst:

```python
name = "avatar-name"   # str  (Text)
hp = 100               # int  (ganze Zahl)
tempo = 3.5            # float (Kommazahl)
lebendig = True        # bool  (True / False)
```

Der Name steht links, der Wert rechts. Später *steht* der Name für den Wert:

```python
print(hp)          # 100
hp = hp - 10       # den alten Wert lesen, einen neuen speichern
print(hp)          # 90
```

!!! note "= ist nicht gleich"
    In der Mathematik heißt `=` „ist gleich“. In Python heißt `=` **„lege diesen
    Wert in diesen Namen“**. Zum *Vergleichen* nutzt du `==` (nächstes Kapitel).

## Typen

Jeder Wert hat einen **Typ**. `type(...)` sagt dir, welchen:

```python
print(type(hp))       # <class 'int'>
print(type(name))     # <class 'str'>
```

| Typ | Beispiel | Ist |
|-----|----------|-----|
| `int` | `42` | ganze Zahl |
| `float` | `3.14` | Kommazahl |
| `str` | `"Grimm"` | Text |
| `bool` | `True` | ja/nein |

Der Typ zählt: `"5" + "5"` ist `"55"` (Text verbunden), aber `5 + 5` ist `10`
(Zahlen addiert). Sie zu mischen ist ein Fehler — `"5" + 5` wirft `TypeError`.

## Sammlungen

Wenn du *viele* Werte brauchst, nimm eine **Liste** (geordnet) oder ein **dict**
(beschriftet):

```python
inventar = ["Schwert", "Brot", "Schlüssel"]   # list
held = {"name": "Hans", "hp": 100}             # dict

print(inventar[0])     # Schwert   — Listen zählen ab 0
print(held["hp"])      # 100       — dicts suchen per Schlüssel

inventar.append("Fackel")   # zur Liste hinzufügen
```

## Probier es

!!! example "Übung — ein Heldenblatt"
    Erstelle Variablen für einen Helden: `name`, `hp` (ein int) und eine
    `inventory`-Liste. Gib einen Satz mit einem f-String aus:
    `f"{name} hat {hp} HP und trägt {inventory}."`

??? tip "Lösung"
    ```python
    --8<-- "snippets/04-hero.py"
    ```

## Zusammenfassung

- Eine **Variable** ist ein Name, der auf einen Wert zeigt; `=` weist zu, `==`
  vergleicht.
- Werte haben **Typen**: `int`, `float`, `str`, `bool`.
- **Listen** sind geordnet (`inventory[0]`), **dicts** suchen per Schlüssel
  (`hero["hp"]`).
- `type(x)` sagt dir den Typ.

## Spickzettel

| Teil | Bedeutet |
|------|----------|
| `x = 5` | `5` in den Namen `x` legen |
| `type(x)` | der Typ von `x` |
| `[1, 2, 3]` | eine Liste (geordnet) |
| `{"k": "v"}` | ein dict (Schlüssel→Wert) |
| `lst[0]` / `d["k"]` | per Index / Schlüssel lesen |

---

**Weiter:** [05 · Debugger](05-debugger.md) — sehen, was dein Code wirklich tut.
