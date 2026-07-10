# 08 · Funktionen

> Gib einem Stück Arbeit einen Namen und nutze es so oft du willst.

## Was du lernst

- Eine Funktion mit `def` definieren
- **Parameter** und **Argumente**
- Einen Wert mit `return` zurückgeben
- Standardwerte

## Die Idee

Eine **Funktion** bündelt Schritte unter einem Namen, damit du sie wieder und
wieder aufrufen kannst (du rufst `print` schon die ganze Zeit auf).

```python
def gruesse(name):
    return f"Hallo {name}!"

print(gruesse("Hänsel"))    # Hallo Hänsel!
print(gruesse("Gretel"))    # Hallo Gretel!
```

- `name` ist ein **Parameter** — ein Platzhalter.
- `"Hänsel"` ist das **Argument** — der echte Wert, den du übergibst.
- `return` gibt einen Wert an die zurück, die die Funktion aufgerufen hat.

Gib Standardwerte, damit ein Argument optional wird:

```python
def braue(staerke=1):
    return "🧪" * staerke

print(braue())     # 🧪
print(braue(3))    # 🧪🧪🧪
```

!!! tip "Print vs. return"
    `print` *zeigt* einen Wert auf dem Bildschirm. `return` *gibt ihn zurück*,
    damit weiterer Code ihn nutzen kann. Funktionen wollen fast immer `return`.

## Probier es

!!! example "Übung"
    Schreibe `schaden(hp, treffer=10)`, das die neue hp nach einem Treffer
    zurückgibt. Ruf es mehrmals auf und füttere das Ergebnis zurück:
    `hp = schaden(hp)`.

---

**Weiter:** [09 · Klassen](09-classes.md) — deine eigenen Baupläne.
