# 01 · Befehle & Aufrufe

> Mit der Maschine sprechen: Befehle in der Shell tippen und Funktionen in Python aufrufen.

## Was du lernst

- Was eine **Shell** ist und wie man einen Befehl ausführt
- Wie man Python startet und eine `.py`-Datei ausführt
- Wie ein **Funktionsaufruf** aussieht — `name(argumente)`
- Dein erster Aufruf: `print(...)`

## Die Idee

Ein **Befehl** ist eine Anweisung, die du in die Shell (dein Terminal) tippst.
Ein **Aufruf** ist, wenn du einem Stück Code sagst, dass es laufen soll — du
nennst seinen Namen und gibst ihm ein paar Werte in Klammern mit.

```python
print("Hallo, Grimm Club!")
```

`print` ist die Funktion. `"Hallo, Grimm Club!"` ist das **Argument**, das du ihr
übergibst. Die Klammern bedeuten „mach es jetzt“.

In der Shell machst du dasselbe mit Programmen:

```sh
python hallo.py         # eine Python-Datei ausführen
python -c "print(2+2)"  # eine Zeile Python ausführen
```

## Probier es

!!! example "Übung"
    1. Öffne dein Terminal (der Editor [micro](https://micro-editor.github.io)
       und eine Shell wurden in **GrimmSetup** eingerichtet).
    2. Tippe `python -c "print('mein Name')"` — ersetze es durch deinen Namen.
    3. Erstelle eine Datei `hallo.py` mit einer `print(...)`-Zeile und führe sie
       mit `python hallo.py` aus.

## Spickzettel

| Du willst… | Befehl |
|------------|--------|
| Eine Python-Datei ausführen | `python datei.py` |
| Eine Zeile ausführen | `python -c "..."` |
| Etwas ausgeben | `print(wert)` |
| Die Python-Shell verlassen | `exit()` |

---

**Weiter:** [02 · Imports](02-imports.md) — Code nutzen, den andere geschrieben haben.
