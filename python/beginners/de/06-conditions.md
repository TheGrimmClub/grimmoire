# 06 · Bedingungen

> Weggabelungen: je nachdem, was wahr ist, Verschiedenes tun.

Geschichten sind voller Entscheidungen — welche Tür, welcher Weg, kämpfen oder
fliehen. Code trifft Entscheidungen mit **Bedingungen**: er stellt eine
Ja/Nein-Frage und führt je nach Antwort verschiedene Zeilen aus.

## Was du lernst

- `if`, `elif`, `else`
- Vergleiche (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Tests verbinden mit `and`, `or`, `not`
- Warum die Einrückung entscheidet, was zum `if` gehört

## if / elif / else

Eine **Bedingung** ist ein Ausdruck, der `True` oder `False` ist. `if` führt
seinen Block nur aus, wenn die Bedingung `True` ist:

```python
hp = 30

if hp <= 0:
    print("Du bist gefallen.")
elif hp < 50:
    print("Vorsicht — wenig Leben!")
else:
    print("Dir geht es gut.")
```

Python prüft von oben nach unten und führt den **ersten** passenden Block aus,
dann überspringt es den Rest. `elif` („else if“) fügt weitere Fälle hinzu; `else`
fängt alles Übrige.

## Vergleiche

Diese Fragen geben `True` oder `False` zurück:

```python
print(hp == 30)   # True   — gleich? (zwei = Zeichen!)
print(hp != 0)    # True   — ungleich
print(hp < 50)    # True   — kleiner als
```

!!! warning "== vs ="
    `=` **weist zu** (`hp = 30`). `==` **vergleicht** (`hp == 30`). `=` zu nutzen,
    wo du `==` meintest, ist der klassische Anfängerfehler.

## Einrückung

Die **Einrückung** (Leerzeichen am Zeilenanfang) sagt Python, welche Zeilen zum
`if` gehören. Gleiche Einrückung = gleicher Block:

```python
if has_key:
    print("Du schließt auf.")   # läuft nur, wenn has_key
    print("Die Tür öffnet sich.")
print("Du gehst weiter.")       # läuft immer — nicht eingerückt
```

## Bedingungen verbinden

```python
has_key = True
at_door = True

if has_key and at_door:      # beide müssen True sein
    print("Die Tür öffnet sich. 🔑")

if tired or hurt:            # mindestens eins True
    print("Du rastest.")

if not alive:                # dreht True/False um
    print("Game over.")
```

## Probier es

!!! example "Übung — welcher Weg?"
    Frag die Spielerin mit `input(...)` nach einer Richtung. Wenn sie `"nord"`
    tippt, gib eine Schatz-Nachricht aus; sonst gib `"Eine Wand versperrt den
    Weg."` aus.

??? tip "Lösung"
    ```python
    --8<-- "snippets/06-direction.py"
    ```

## Zusammenfassung

- `if` / `elif` / `else` wählen einen Block nach dem, was `True` ist; der erste
  Treffer gewinnt.
- Vergleiche mit `==`, `!=`, `<`, `>`, `<=`, `>=` — nicht `=`.
- Die **Einrückung** entscheidet, was zum `if` gehört.
- Verbinde mit `and`, `or`, `not`.

## Spickzettel

| Operator | Bedeutet |
|----------|----------|
| `==` / `!=` | gleich / ungleich |
| `<` `>` `<=` `>=` | Größen vergleichen |
| `and` | beide müssen wahr sein |
| `or` | mindestens eins wahr |
| `not` | dreht wahr/falsch um |

---

**Weiter:** [07 · Schleifen & Steuerung](07-loops-and-loop-controls.md).
