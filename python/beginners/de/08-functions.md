# 08 · Funktionen

> Gib einem Stück Arbeit einen Namen und nutze es so oft du willst.

Du *rufst* seit [Kapitel 01](01-commands-and-calls.md) Funktionen auf —
`print(...)`. Jetzt schreibst du deine eigenen. Eine Funktion lässt dich ein paar
Schritte nehmen, ihnen einen Namen geben und sie wieder und wieder ausführen,
ohne dich zu wiederholen.

## Was du lernst

- Eine Funktion mit `def` definieren
- **Parameter** vs. **Argumente**
- Einen Wert mit `return` zurückgeben
- Standardwerte, damit ein Argument optional wird
- Warum `return` nicht dasselbe ist wie `print`

## Definieren und aufrufen

```python
def gruesse(name):
    return f"Hallo {name}!"

print(gruesse("Hänsel"))    # Hallo Hänsel!
print(gruesse("Gretel"))    # Hallo Gretel!
```

- `def` beginnt die Definition.
- `gruesse` ist der **Name**.
- `name` ist ein **Parameter** — ein Platzhalter, der gefüllt wird, wenn die
  Funktion aufgerufen wird.
- Die eingerückten Zeilen sind der **Körper** — was läuft, wenn du sie aufrufst.

`"Hänsel"` ist ein **Argument**: der echte Wert, den du für `name` übergibst.
Parameter = der Name in der Definition; Argument = der Wert beim Aufruf.

## `return`: einen Wert zurückgeben

`return` sendet einen Wert an die zurück, die die Funktion aufgerufen hat, und
beendet sie:

```python
def verdopple(x):
    return x * 2

ergebnis = verdopple(21)    # ergebnis ist jetzt 42
print(ergebnis)
```

Der Aufruf `verdopple(21)` *wird* zu `42`, also kannst du ihn speichern, ausgeben
oder in einen anderen Aufruf füttern. Eine Funktion ohne `return` gibt `None`
zurück (nichts).

!!! warning "return ist nicht print"
    `print` **zeigt** einen Wert auf dem Bildschirm und wirft ihn weg. `return`
    **gibt ihn zurück**, damit weiterer Code ihn nutzen kann.

    ```python
    def addiere(a, b):
        print(a + b)      # zeigt es, aber du kannst es nicht wiederverwenden
    summe = addiere(2, 3) # gibt 5 aus, aber summe ist None!
    ```
    ```python
    def addiere(a, b):
        return a + b      # ✓ gibt es zurück
    summe = addiere(2, 3) # summe ist 5
    ```

## Standardwerte

Gib einem Parameter einen Standardwert, und das Argument wird optional (du hast
das mit `Actor(name="Namenloser")` im Klassen-Kapitel gesehen):

```python
def braue(staerke=1):
    return "🧪" * staerke

print(braue())     # 🧪
print(braue(3))    # 🧪🧪🧪
```

## Ausführliches Beispiel

Ein winziger Kampfschritt, aus Funktionen gebaut:

```python
def schaden(hp, treffer=10):
    return hp - treffer

hp = 100
hp = schaden(hp)        # 90
hp = schaden(hp, 25)    # 65
print("HP:", hp)
```

Jeder Aufruf nimmt die aktuelle `hp` und gibt eine neue zurück — du fütterst das
Ergebnis zurück. Kleine Funktionen, kombiniert, werden zu einem Programm.

## Probier es

!!! example "Übung 1 — laut grüßen"
    Schreibe `shout(text)`, das `text` in Großbuchstaben zurückgibt (Tipp:
    Strings haben eine Methode `.upper()`). Teste es mit `print(shout("hallo"))`.
    (Bezeichner im Code sind auf Englisch — nur die Erzählung ist Deutsch.)

!!! example "Übung 2 — heilen"
    Schreibe `heal(hp, amount=20)`, das die neue hp zurückgibt. Verkette ein paar
    `damage`- und `heal`-Aufrufe und füttere das Ergebnis jedes Mal zurück.

??? tip "Lösung für Übung 1"
    ```python
    --8<-- "snippets/08-shout.py"
    ```

## Zusammenfassung

- `def name(parameter):` definiert eine Funktion; der Körper ist eingerückt.
- **Parameter** = Platzhalter in der Definition; **Argument** = Wert beim Aufruf.
- `return` gibt einen Wert zurück (die meisten Funktionen wollen das); kein
  `return` → `None`.
- **Standardwerte** machen Argumente optional.

## Spickzettel

| Teil | Bedeutet |
|------|----------|
| `def f(x):` | eine Funktion mit Parameter `x` definieren |
| `return v` | `v` zurückgeben und stoppen |
| `f(3)` | `f` mit Argument `3` aufrufen |
| `def f(x=1):` | `x` hat Standardwert `1` |

---

**Weiter:** [09 · Klassen](09-classes.md) — deine eigenen Baupläne.
