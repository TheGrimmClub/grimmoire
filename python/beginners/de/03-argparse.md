# 03 · argparse

> Lass dein Programm Befehle annehmen: Argumente von der Kommandozeile lesen.

Ein Programm wird nützlich, wenn die Person, die es ausführt, es steuern kann —
so wie du in [Kapitel 01](01-commands-and-calls.md) die Shell gesteuert hast.
`argparse` verwandelt die Wörter nach `python deinskript.py` in ordentliche,
benannte Werte.

## Was du lernst

- Der Unterschied zwischen `sys.argv` und `argparse`
- Ein Argument mit Name, Typ und Hilfetext definieren
- Positionsargumente vs. `--optionen`
- Das gratis `--help`, das du geschenkt bekommst

## Der rohe Weg: `sys.argv`

Alles, was nach `python` getippt wird, landet in einer Liste namens `sys.argv`:

```python
import sys
print(sys.argv)     # ['gruss.py', 'Nord', '--laut']
```

`sys.argv[0]` ist der Skriptname; der Rest ist, was die Nutzerin getippt hat. Es
funktioniert, aber *du* musst herausfinden, was jedes Wort bedeutet. Das wird
schnell unübersichtlich.

## Der gute Weg: `argparse`

`argparse` zerlegt die Kommandozeile für dich und schreibt sogar den Hilfetext:

```python
import argparse

parser = argparse.ArgumentParser(description="Begrüße eine Grimm-Heldin.")
parser.add_argument("name", help="der Name der Heldin")
parser.add_argument("--shout", action="store_true", help="in Großbuchstaben")
args = parser.parse_args()

greeting = f"Hallo {args.name}"
print(greeting.upper() if args.shout else greeting)
```

Führe es aus:

```sh
python gruss.py Hänsel            # Hallo Hänsel
python gruss.py Hänsel --shout    # HALLO HÄNSEL
python gruss.py --help            # Hilfetext, für dich geschrieben
```

## Positional vs. optional

- **Positional** (`"name"`) — nötig, erkannt an *seiner Stelle*.
- **Optional** (`"--shout"`) — beginnt mit `--`, erkannt am *Namen*, meist
  optional.

Zwei praktische Arten optionaler Argumente:

```python
parser.add_argument("--shout", action="store_true")  # ein Schalter: an/aus
parser.add_argument("--hp", type=int, default=100)    # ein Wert, zu int gewandelt
```

`action="store_true"` macht einen Schalter, der `False` ist, außer die Nutzerin
fügt ihn hinzu. `type=int` wandelt den Text `"25"` in die Zahl `25`.

!!! tip "Du bekommst --help gratis"
    Weil du jedes Argument beschrieben hast, gibt `python gruss.py --help` eine
    vollständige Benutzung aus. Gute Werkzeuge erklären sich selbst.

## Probier es

!!! example "Übung — betritt das Verlies"
    Schreibe `enter.py`, das ein Positionsargument `name` nimmt und
    `f"{name} betritt das Verlies."` ausgibt. Füge ein optionales `--torch`
    hinzu, das zusätzlich `🕯️` ausgibt.

??? tip "Lösung"
    ```python
    --8<-- "snippets/03-enter.py"
    ```
    ```sh
    python enter.py Gretel --torch
    ```

## Zusammenfassung

- `sys.argv` ist die rohe Liste; `argparse` macht daraus benannte Werte.
- **Positional**-Argumente sind nach Stelle nötig; **`--optionen`** sind benannt.
- `action="store_true"` = ein Schalter; `type=int` wandelt Text in eine Zahl.
- Du bekommst `--help` gratis.

## Spickzettel

| Teil | Tut |
|------|-----|
| `add_argument("name")` | ein nötiger Positionswert |
| `add_argument("--flag", action="store_true")` | ein Ein/Aus-Schalter |
| `add_argument("--n", type=int)` | in eine Zahl umwandeln |
| `parse_args()` | die echte Kommandozeile lesen |

---

**Weiter:** [04 · Variablen & Werte](04-variables-and-values.md).
