# 03 · argparse

> Lass dein Programm Befehle annehmen: Argumente von der Kommandozeile lesen.

## Was du lernst

- Der Unterschied zwischen `sys.argv` und `argparse`
- Wie man ein Argument mit Name, Typ und Hilfetext definiert
- Wie man ein Skript mit Optionen ausführt

## Die Idee

Programme werden nützlich, wenn die Nutzerin sie steuern kann. Der rohe Weg ist
`sys.argv` (eine Liste der Wörter, die nach `python` getippt wurden):

```python
import sys
print(sys.argv)   # ['skript.py', 'Nord', '--laut']
```

`argparse` erledigt das mühsame Zerlegen für dich und liefert gratis `--help`:

```python
import argparse

parser = argparse.ArgumentParser(description="Begrüße eine Grimm-Heldin.")
parser.add_argument("name", help="der Name der Heldin")
parser.add_argument("--shout", action="store_true", help="in Großbuchstaben")
args = parser.parse_args()

gruss = f"Hallo {args.name}"
print(gruss.upper() if args.shout else gruss)
```

```sh
python gruss.py Hänsel --shout   # HALLO HÄNSEL
python gruss.py --help           # argparse zeigt die Benutzung gratis
```

## Probier es

!!! example "Übung"
    Schreibe `betrete.py`, das ein Argument `name` nimmt und
    `f"{name} betritt das Verlies."` ausgibt. Füge ein optionales `--fackel`
    hinzu, das zusätzlich `🕯️` ausgibt.

## Spickzettel

| Teil | Tut |
|------|-----|
| `add_argument("name")` | ein nötiger Positionswert |
| `add_argument("--flag", action="store_true")` | ein Ein/Aus-Schalter |
| `add_argument("--n", type=int)` | in eine Zahl umwandeln |
| `parse_args()` | die echte Kommandozeile lesen |

---

**Weiter:** [04 · Variablen & Werte](04-variables-and-values.md).
