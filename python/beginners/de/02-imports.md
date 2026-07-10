# 02 · Imports

> Auf den Schultern von Riesen stehen: Code aus anderen Dateien und Bibliotheken nutzen.

Du fängst fast nie bei null an. Python kommt mit einer riesigen
**Standardbibliothek**, und die Welt hat Millionen weitere Pakete geschrieben.
**Importieren** ist, wie du an diese Arbeit kommst, statt sie neu zu schreiben.

## Was du lernst

- Was ein **Modul** und ein **Paket** sind
- `import x` vs. `from x import y`
- Wie Umbenennen mit `as` hilft
- Wo Python nach Dingen zum Importieren sucht
- Das berühmte Osterei, `import antigravity`

## Modul und Paket

Ein **Modul** ist eine einzelne `.py`-Datei voller Code. Ein **Paket** ist ein
Ordner voller Module, die zusammengehören. So oder so greifst du mit `import`
hinein.

```python
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
```

`import math` holt das ganze Modul; an seinen Inhalt kommst du dann mit einem
Punkt: `math.sqrt`, `math.pi`.

## `from ... import ...`

Wenn du nur ein oder zwei Dinge brauchst, importiere sie beim Namen und spar dir
das Präfix:

```python
from math import sqrt, pi
print(sqrt(16))    # kein "math." nötig
print(pi)
```

Das eigene Paket des Clubs funktioniert genauso:

```python
from grimm import Actor
me = Actor()
print(me)
```

## Umbenennen mit `as`

Manchmal ist ein Name lang oder kollidiert mit deinem eigenen. `as` gibt ihm
einen Spitznamen:

```python
import statistics as stats
print(stats.mean([1, 2, 3]))   # 2

from grimm import Actor as Held
me = Held(name="Hans")
```

## Woher Imports kommen

`import x` findet `x`, wenn es Teil von Pythons Standardbibliothek ist, in deiner
Umgebung installiert ist (per `uv add`) oder eine Datei neben deinem Programm.
Deshalb funktioniert `from grimm import Actor`, sobald du im
`grimm__python__zero`-Projekt bist — der Ordner `grimm/` liegt direkt da.

!!! warning "Überdecke die Standardbibliothek nicht"
    Wenn du deine eigene Datei `math.py` oder `random.py` nennst, findet
    `import math` vielleicht *deine* Datei statt Pythons und verhält sich seltsam.
    Benenne Dateien nicht nach Modulen, die du importierst.

!!! tip "Probier das Osterei"
    Tippe `import antigravity` in einer Python-Shell. Python machte schon Witze,
    bevor du geboren wurdest. (`grimm.Dungeon` — [Kapitel 09](09-classes.md) —
    spielt mit derselben Idee.)

## Probier es

!!! example "Übung 1 — zufällige Richtung"
    `import random`, dann gib `random.choice(["Nord", "Süd", "Ost", "West"])` aus.
    Führe es ein paar Mal aus.

!!! example "Übung 2 — dein Paket"
    Klone [grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero),
    dann führe in einer REPL `from grimm import Actor` aus und erstelle einen.

??? tip "Lösung für Übung 1"
    <!-- snippet: 02-random-direction.py -->
    ```python
    import random

    print("Du gehst nach", random.choice(["Nord", "Süd", "Ost", "West"]))
    ```
    <!-- endsnippet -->

## Zusammenfassung

- Ein **Modul** ist eine Datei; ein **Paket** ist ein Ordner voller Module.
- `import x` holt das Ganze (`x.ding`); `from x import y` holt einen Namen.
- `as` benennt einen Import um.
- Benenne deine Dateien nicht nach Modulen, die du importierst.

## Spickzettel

| Form | Bedeutung |
|------|-----------|
| `import math` | ganzes Modul; nutze `math.sqrt` |
| `from math import sqrt` | nur `sqrt` |
| `import numpy as np` | in `np` umbenennen |
| `from grimm import Actor` | ein Name aus einem Paket |

---

**Weiter:** [03 · argparse](03-argparse.md) — Eingaben von der Kommandozeile lesen.
