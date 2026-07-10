# 05 · Debugger

> Wenn Code sich schlecht benimmt, hör auf zu raten — schau ihm beim Laufen zu.

## Was du lernst

- Debuggen mit `print(...)` (einfach und ehrlich)
- Ein Programm mit `breakpoint()` anhalten
- Die wichtigsten `pdb`-Griffe: Schritt, weiter, ansehen

## Die Idee

Code funktioniert selten beim ersten Mal. Das ist normal (siehe das
[Manifest](00-manifest.md)). Debuggen ist, wie du *siehst*, was passiert.

Das einfachste Werkzeug ist `print`:

```python
summe = 0
for muenze in [1, 5, 10]:
    summe = summe + muenze
    print("Summe ist jetzt", summe)   # beim Wachsen zusehen
```

Das echte Werkzeug ist der **Debugger**. Setze `breakpoint()` in deinen Code,
und Python hält dort an und gibt dir eine Eingabe:

```python
def braue(a, b):
    breakpoint()      # die Ausführung pausiert hier
    return a + b
```

An der `(Pdb)`-Eingabe:

| Tippe | Tut |
|-------|-----|
| `p summe` | eine Variable ausgeben (**p**rint) |
| `n` | nächste Zeile (**n**ext) |
| `s` | in eine Funktion springen (**s**tep) |
| `c` | weiterlaufen (**c**ontinue) |
| `q` | beenden (**q**uit) |

## Probier es

!!! example "Übung"
    Nimm eine Schleife, die Zahlen absichtlich falsch addiert, füge ein
    `breakpoint()` ein und finde mit `p` und `n` die genaue Zeile, in der die
    Summe abweicht.

!!! note "Editor & IDE"
    Editoren wie VS Code haben einen visuellen Debugger — dieselben Ideen,
    Knöpfe statt Buchstaben. Lern zuerst die Buchstaben; die funktionieren
    überall, sogar über SSH.

---

**Weiter:** [06 · Bedingungen](06-conditions.md) — Entscheidungen treffen.
