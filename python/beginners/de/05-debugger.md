# 05 · Debugger

> Wenn Code sich schlecht benimmt, hör auf zu raten — schau ihm beim Laufen zu.

Code funktioniert selten beim ersten Mal. Das ist normal — das
[Manifest](00-manifest.md) sagt es. Feststecken ist kein Versagen; es ist ein
Punkt auf der Karte. Debuggen ist, wie du *siehst*, was dein Code wirklich tut,
statt zu raten.

## Was du lernst

- Debuggen mit `print(...)` — einfach und ehrlich
- Ein Programm mit `breakpoint()` anhalten
- Die wichtigsten `pdb`-Griffe: print, next, step, continue
- Wie man eine Fehlermeldung liest

## Eine Fehlermeldung lesen

Wenn Python mit einem Fehler stoppt, lies ihn **von unten nach oben**:

```
Traceback (most recent call last):
  File "spell.py", line 3, in <module>
    print(hp + name)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Die letzte Zeile ist, *was* schiefging (`TypeError`, ein int und ein str
addiert). Das `File ... line 3` ist *wo*. Die meisten Korrekturen beginnen damit,
diese unterste Zeile sorgfältig zu lesen.

## Print-Debugging

Das einfachste Werkzeug ist `print` — streu es ein, um Werte beim Wachsen zu
beobachten:

```python
total = 0
for coin in [1, 5, 10]:
    total = total + coin
    print("total ist jetzt", total)   # 1, dann 6, dann 16
```

Ehrlich, schnell, funktioniert überall. Denk nur daran, sie danach zu entfernen.

## Der echte Debugger

`breakpoint()` **pausiert** dein Programm und wirft dich in eine interaktive
Eingabe, mitten im Lauf:

```python
def brew(a, b):
    breakpoint()      # die Ausführung stoppt hier
    return a + b
```

An der `(Pdb)`-Eingabe steuerst du:

| Tippe | Tut |
|-------|-----|
| `p total` | den Wert einer Variablen ausgeben (**p**rint) |
| `n` | nächste Zeile (**n**ext) |
| `s` | in einen Funktionsaufruf springen (**s**tep) |
| `c` | weiterlaufen (**c**ontinue) |
| `q` | beenden (**q**uit) |

Du darfst dich *umsehen*, während das Programm eingefroren ist — jede Variable
prüfen, Zeile für Zeile vorgehen und genau sehen, wo etwas schiefläuft.

## Probier es

!!! example "Übung — auf frischer Tat ertappen"
    Nimm die Münzschleife unten, setz ein `breakpoint()` hinein und nutze
    `p total` und `n`, um die Summe Münze für Münze wachsen zu sehen.

??? tip "Lösung"
    ```python
    --8<-- "snippets/05-fix.py"
    ```

!!! note "Editor & IDE"
    Editoren wie VS Code haben einen visuellen Debugger — dieselben Ideen, Knöpfe
    statt Buchstaben. Lern zuerst die Buchstaben; die funktionieren überall, sogar
    über SSH.

## Zusammenfassung

- Lies Tracebacks **von unten nach oben**: die letzte Zeile sagt was und wo.
- `print(...)` ist schnelles, ehrliches Debuggen.
- `breakpoint()` pausiert das Programm; `p`, `n`, `s`, `c`, `q` steuern es.

## Spickzettel

| Teil | Tut |
|------|-----|
| `breakpoint()` | pausieren und den Debugger öffnen |
| `p x` | Variable `x` ausgeben |
| `n` / `s` | nächste Zeile / hineinspringen |
| `c` / `q` | weiter / beenden |

---

**Weiter:** [06 · Bedingungen](06-conditions.md) — Entscheidungen treffen.
