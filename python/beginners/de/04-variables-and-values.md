# 04 · Variablen & Werte

> Dingen Namen geben, damit dein Programm sie sich merken kann.

## Was du lernst

- Was eine **Variable** ist (ein Name, der auf einen Wert zeigt)
- Die alltäglichen **Typen**: `int`, `float`, `str`, `bool`
- Sammlungen: `list` und `dict`
- Wie man einen Wert mit `type(...)` untersucht

## Die Idee

Eine **Variable** ist ein Etikett, das du auf einen Wert klebst:

```python
name = "avatar-name"   # str  (Text)
leben = 100            # int  (ganze Zahl)
tempo = 3.5            # float (Kommazahl)
lebendig = True        # bool  (True / False)
```

Werte haben **Typen**. `type(...)` sagt dir, welchen:

```python
print(type(leben))     # <class 'int'>
```

Sammlungen halten viele Werte:

```python
inventar = ["Schwert", "Brot", "Schlüssel"]   # list — geordnet
held = {"name": "Hans", "hp": 100}             # dict — Schlüssel → Wert

print(inventar[0])     # Schwert
print(held["hp"])      # 100
```

## Probier es

!!! example "Übung"
    Erstelle Variablen für einen Helden: `name`, `hp` und eine `inventar`-Liste.
    Gib einen Satz mit einem f-String aus:
    `f"{name} hat {hp} HP und trägt {inventar}."`

## Spickzettel

| Typ | Beispiel | Ist |
|-----|----------|-----|
| `int` | `42` | ganze Zahl |
| `float` | `3.14` | Kommazahl |
| `str` | `"Grimm"` | Text |
| `bool` | `True` | ja/nein |
| `list` | `[1, 2, 3]` | geordnete Sammlung |
| `dict` | `{"k": "v"}` | Schlüssel→Wert-Zuordnung |

---

**Weiter:** [05 · Debugger](05-debugger.md) — sehen, was dein Code wirklich tut.
