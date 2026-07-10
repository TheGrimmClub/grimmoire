# 07 · Schleifen & Steuerung

> Etwas wiederholen — und wissen, wann man aufhört.

## Was du lernst

- `for`-Schleifen über eine Sammlung
- `while`-Schleifen, bis sich eine Bedingung ändert
- `range(...)` zum Zählen
- `break` und `continue`, um eine Schleife zu lenken

## Die Idee

Eine **Schleife** wiederholt einen Block. Eine `for`-Schleife geht durch eine
Sammlung:

```python
for gegenstand in ["Schwert", "Brot", "Schlüssel"]:
    print("Du trägst:", gegenstand)
```

Zählen mit `range`:

```python
for i in range(3):        # 0, 1, 2
    print("Schritt", i)
```

Eine `while`-Schleife läuft, bis ihre Bedingung `False` wird:

```python
fackeln = 3
while fackeln > 0:
    print("Eine Fackel brennt.")
    fackeln = fackeln - 1
```

Von innen lenken:

```python
for tuer in tueren:
    if tuer == "verschlossen":
        continue       # diese überspringen, zur nächsten
    if tuer == "Ausgang":
        break          # die Schleife ganz verlassen
```

!!! warning "Endlosschleife"
    Ein `while`, dessen Bedingung nie `False` wird, läuft ewig. Sorge dafür, dass
    sich innen etwas ändert. `Strg+C` stoppt ein außer Kontrolle geratenes
    Programm.

## Probier es

!!! example "Übung"
    Geh mit `range(1, 11)` durch und gib nur die geraden Zahlen aus (Tipp:
    `% 2 == 0`).

---

**Weiter:** [08 · Funktionen](08-functions.md) — einem Stück Arbeit einen Namen geben.
