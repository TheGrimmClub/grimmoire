# 06 · Bedingungen

> Weggabelungen: je nachdem, was wahr ist, Verschiedenes tun.

## Was du lernst

- `if`, `elif`, `else`
- Vergleiche (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Tests verbinden mit `and`, `or`, `not`
- Warum Einrückung in Python wichtig ist

## Die Idee

Eine **Bedingung** ist eine Frage mit einer Ja/Nein-Antwort. `if` führt einen
Block nur aus, wenn die Antwort `True` ist:

```python
hp = 30

if hp <= 0:
    print("Du bist gefallen.")
elif hp < 50:
    print("Vorsicht — wenig Leben!")
else:
    print("Dir geht es gut.")
```

Die **Einrückung** (die Leerzeichen am Zeilenanfang) sagt Python, welche Zeilen
zum `if` gehören. Gleiche Einrückung = gleicher Block.

Fragen verbinden:

```python
hat_schluessel = True
an_tuer = True

if hat_schluessel and an_tuer:
    print("Die Tür öffnet sich. 🔑")
```

## Probier es

!!! example "Übung"
    Frage nach einer Richtung (`"nord"`, `"süd"`, …). Wenn es `"nord"` ist, gib
    eine Schatz-Nachricht aus; bei allem anderen „Eine Wand versperrt den Weg.“

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
