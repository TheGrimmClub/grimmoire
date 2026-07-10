# 07 · Schleifen & Steuerung

> Etwas wiederholen — und wissen, wann man aufhört.

Computer sind großartig im Wiederholen. Eine **Schleife** führt denselben Block
viele Male aus, sodass du ihn einmal schreibst, statt ihn hundertmal zu kopieren.

## Was du lernst

- `for`-Schleifen über eine Sammlung
- `while`-Schleifen, bis sich eine Bedingung ändert
- `range(...)` zum Zählen
- `break` und `continue`, um eine Schleife zu lenken

## for: durch eine Sammlung gehen

Eine `for`-Schleife nimmt jeden Gegenstand einer Sammlung der Reihe nach:

```python
for item in ["Schwert", "Brot", "Schlüssel"]:
    print("Du trägst:", item)
```

Der eingerückte Körper läuft einmal pro Gegenstand, mit `item` auf jeden Wert
gesetzt.

## range: zählen

`range` macht eine Folge von Zahlen — praktisch, um eine feste Anzahl von Malen
zu wiederholen:

```python
for i in range(3):        # 0, 1, 2
    print("Schritt", i)

for i in range(1, 4):     # 1, 2, 3  (Start, Stopp)
    print(i)
```

`range(n)` stoppt *vor* `n`, also gibt `range(3)` `0, 1, 2` — drei Werte.

## while: bis sich eine Bedingung ändert

Eine `while`-Schleife wiederholt, **solange** ihre Bedingung `True` ist:

```python
torches = 3
while torches > 0:
    print("Eine Fackel brennt.")
    torches = torches - 1     # bewege dich zum Ende!
```

!!! warning "Endlosschleife"
    Wenn die Bedingung nie `False` wird, läuft die Schleife ewig. Sorge dafür,
    dass sich innen etwas ändert. `Strg+C` stoppt ein außer Kontrolle geratenes
    Programm.

## break und continue

Lenke eine Schleife von innen:

```python
for door in doors:
    if door == "verschlossen":
        continue       # diese überspringen, zur nächsten
    if door == "Ausgang":
        break          # die Schleife ganz verlassen
    print("Du öffnest:", door)
```

- `continue` — den Rest *dieser* Runde überspringen, zur nächsten.
- `break` — die ganze Schleife jetzt stoppen.

## Probier es

!!! example "Übung — nur die geraden"
    Geh mit `range(1, 11)` durch und gib nur die geraden Zahlen aus. Tipp: eine
    Zahl ist gerade, wenn `n % 2 == 0` (`%` ist der Rest).

??? tip "Lösung"
    ```python
    --8<-- "snippets/07-evens.py"
    ```

## Zusammenfassung

- `for` geht durch eine Sammlung; `while` wiederholt, bis eine Bedingung kippt.
- `range(n)` zählt `0 … n-1`; `range(a, b)` zählt `a … b-1`.
- `continue` überspringt eine Runde; `break` beendet die Schleife.
- Sorge immer dafür, dass ein `while` enden kann.

## Spickzettel

| Teil | Tut |
|------|-----|
| `for x in seq:` | einmal pro Gegenstand laufen |
| `range(n)` | `0 … n-1` |
| `while cond:` | wiederholen, solange `cond` wahr ist |
| `continue` / `break` | eine Runde überspringen / die Schleife beenden |

---

**Weiter:** [08 · Funktionen](08-functions.md) — einem Stück Arbeit einen Namen geben.
