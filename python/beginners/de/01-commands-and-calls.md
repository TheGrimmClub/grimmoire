# 01 · Befehle & Aufrufe

> Mit der Maschine sprechen: Befehle in der Shell tippen und Funktionen in Python aufrufen.

Jede Reise in der Grimm-Welt beginnt mit einem einzigen Wort, das man ins Dunkel
tippt. In diesem Kapitel geht es um dieses erste Gespräch mit dem Computer — wie
du ihm eine Anweisung gibst und wie er antwortet.

## Was du lernst

- Was eine **Shell** ist und wie man einen Befehl ausführt
- Wie man Python startet und eine `.py`-Datei ausführt
- Wie ein **Funktionsaufruf** aussieht — `name(argumente)`
- Deinen ersten Aufruf, `print(...)`, und wie man seine Ausgabe liest
- Wie man die drei Fehler behebt, die am ersten Tag alle machen

## Die Shell: deine erste Tür

Die **Shell** (auch „Terminal“ oder „Konsole“) ist ein Programm, das darauf
wartet, dass du einen **Befehl** tippst und Enter drückst. Sie führt den Befehl
aus und zeigt das Ergebnis. Es ist einfach ein Gespräch: du sagst etwas, sie
antwortet.

```sh
python --version      # frag, welches Python du hast
```

```
Python 3.13.0
```

Du hast einen Befehl getippt; die Shell hat geantwortet. Das ist die ganze
Schleife, für immer.

!!! tip "Wo ist meine Shell?"
    Sie wurde an Tag eins in
    [GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup) eingerichtet,
    zusammen mit dem Editor [micro](https://micro-editor.github.io). Auf macOS
    heißt sie *Terminal*, auf Windows die *Git-Bash*-Shell, auf Linux jede
    Terminal-App.

## Python ausführen

Es gibt drei Wege, Python auszuführen, vom schnellsten zum nützlichsten:

```sh
python                       # 1. eine interaktive Sitzung starten (eine REPL)
python -c "print(2 + 2)"     # 2. eine Zeile ausführen und beenden
python hallo.py              # 3. eine ganze Datei ausführen
```

Die **REPL** (Read–Eval–Print Loop) ist eine Python-Shell *innerhalb* deiner
Shell. Du tippst Python, sie antwortet sofort. Verlasse sie mit `exit()`.

```python
>>> 2 + 2
4
>>> exit()
```

## Aufrufe: Code sagen, dass er laufen soll

Ein **Aufruf** ist, wenn du einem Stück Code sagst, dass es seine Arbeit tun
soll. Du schreibst seinen **Namen**, dann runde Klammern `()` mit allen Werten,
die es braucht, darin:

```python
print("Hallo, Grimm Club!")
```

- `print` — der **Name** der Funktion.
- `"Hallo, Grimm Club!"` — das **Argument**, der Wert, den du ihr übergibst.
- `()` — die Klammern bedeuten *„mach es jetzt“*.

Ohne die Klammern *zeigst* du nur auf die Funktion, du führst sie nicht aus:

```python
print          # <built-in function print>  — nichts passiert
print()        # (gibt eine leere Zeile aus) — sie läuft
```

Du kannst mehr als ein Argument übergeben, getrennt durch Kommas:

```python
print("HP:", 100)     # HP: 100
```

## Eine erste Datei

Öffne deinen Editor und erstelle `hallo.py`:

```python
print("Ich betrete den Wald.")
print("Es ist dunkel.")
```

Führe sie aus:

```sh
python hallo.py
```

```
Ich betrete den Wald.
Es ist dunkel.
```

Python führt die Datei **von oben nach unten** aus, eine Zeile nach der anderen.
Die Reihenfolge zählt.

## Drei Fehler am ersten Tag

!!! warning "Achtung"
    - **Anführungszeichen vergessen:** `print(Hallo)` sucht nach einer *Variablen*
      namens `Hallo` und wirft einen Fehler. Text braucht Anführungszeichen:
      `print("Hallo")`.
    - **Klammern vergessen:** `print "hi"` ist in Python 3 kein Aufruf — es ist
      ein `SyntaxError`. Immer `print("hi")`.
    - **Falscher Ordner:** `python hallo.py` funktioniert nur, wenn du *in* dem
      Ordner bist, der `hallo.py` enthält. Nutze `ls` (macOS/Linux) oder `dir`
      (Windows), um dich umzusehen.

## Probier es

!!! example "Übung 1 — dein Name"
    Gib in der REPL deinen Namen aus: `print("...")`. Gib dann deinen Namen und
    dein Alter in einer Zeile mit einem Komma aus.

!!! example "Übung 2 — eine kleine Szene"
    Erstelle eine Datei `wald.py` mit drei `print(...)`-Zeilen, die eine
    Mini-Szene im Wald erzählen. Führe sie mit `python wald.py` aus.

??? tip "Steckst du fest? Eine Musterlösung"
    ```python
    # wald.py
    print("Ich stehe am Waldrand.")
    print("Drei Männlein winken mir zu.")
    print("Ich gehe hinein.")
    ```
    ```sh
    python wald.py
    ```

## Zusammenfassung

- Die **Shell** führt **Befehle** aus; Python läuft aus der REPL, per `-c` oder
  aus einer Datei.
- Ein **Aufruf** ist `name(argumente)` — die Klammern lassen ihn *jetzt* laufen.
- `print(...)` zeigt Werte; Text braucht `"Anführungszeichen"`.

## Spickzettel

| Du willst… | Befehl |
|------------|--------|
| Dein Python prüfen | `python --version` |
| Die REPL starten | `python` (verlassen mit `exit()`) |
| Eine Zeile ausführen | `python -c "..."` |
| Eine Datei ausführen | `python datei.py` |
| Etwas ausgeben | `print(wert)` |

---

**Weiter:** [02 · Imports](02-imports.md) — Code nutzen, den andere geschrieben haben.
