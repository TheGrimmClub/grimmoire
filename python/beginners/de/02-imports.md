# 02 · Imports

> Auf den Schultern von Riesen stehen: Code aus anderen Dateien und Bibliotheken nutzen.

## Was du lernst

- Was ein **Modul** und ein **Paket** sind
- `import x` vs. `from x import y`
- Wo Python nach Dingen zum Importieren sucht
- Das berühmte Osterei: `import antigravity`

## Die Idee

Du fängst fast nie bei null an. **Importieren** holt Code herein, den jemand
anderes (oder du, früher) schon geschrieben hat.

```python
import math
print(math.sqrt(16))      # 4.0

from math import sqrt
print(sqrt(16))           # dasselbe, kürzer
```

Ein **Modul** ist eine `.py`-Datei. Ein **Paket** ist ein Ordner voller Module.
Das eigene Paket des Clubs heißt `grimm`:

```python
from grimm import Actor
me = Actor()
print(me)
```

!!! tip "Probier das Osterei"
    Tippe `import antigravity` in einer Python-Shell. Python machte schon Witze,
    bevor du geboren wurdest.

## Probier es

!!! example "Übung"
    1. `import random` und gib `random.choice(["Nord", "Süd", "Ost", "West"])` aus.
    2. Klone [grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero)
       und führe `from grimm import Actor` aus.

## Spickzettel

| Form | Bedeutung |
|------|-----------|
| `import math` | das ganze Modul; nutze `math.sqrt` |
| `from math import sqrt` | nur `sqrt` holen |
| `import math as m` | in `m` umbenennen |
| `from grimm import Actor` | ein Name aus einem Paket |

---

**Weiter:** [03 · argparse](03-argparse.md) — Eingaben von der Kommandozeile lesen.
