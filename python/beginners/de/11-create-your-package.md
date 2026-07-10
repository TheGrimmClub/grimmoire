# 11 · Baue dein Paket

> Veröffentliche etwas Echtes: mach aus deinem Code ein Paket, das andere installieren können.

Das ist die Ziellinie des Anfängerpfads. Alles bisher — Aufrufe, Imports,
Variablen, Funktionen, Klassen, uv — kommt hier zu einem **Paket** zusammen:
einem ordentlichen Bündel aus Code, das jeder per `pip install` installieren und
`import`-ieren kann.

## Was du lernst

- Die Form eines Python-Pakets (`pyproject.toml` + ein Quellordner)
- Wie `from deinpaket import Ding` funktioniert
- Tests hinzufügen
- Was „veröffentlichen“ bedeutet

## Die Form eines Pakets

Ein **Paket** ist ein Ordner voller Module plus eine `pyproject.toml`, die es
beschreibt. Du hast schon eins gesehen:
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

```
grimm-first/
├── pyproject.toml      # Name, Version, nötiges Python, Abhängigkeiten
├── grimm/              # das Paket — importierbar als `grimm`
│   ├── __init__.py     # Re-Exports: from grimm import Actor
│   └── actor.py        # dein Code
└── tests/
    └── test_actor.py   # Beweis, dass es funktioniert
```

Der Ordner `grimm/` **ist** das Paket: sein Name ist der Name, den du
`import`-ierst. Die Datei `__init__.py` macht ihn erst zum Paket, und dort wählst
du, was re-exportiert wird.

## `pyproject.toml`

Diese eine Datei beschreibt dein Projekt für Python und für die Welt:

```toml
[project]
name = "grimm-first"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- `name` ist der **Distributions**-Name (was Leute per `pip install` holen).
- `version` — erhöhe sie bei jeder Veröffentlichung.
- `dependencies` — andere Pakete, die deins braucht (uv füllt diese beim
  `uv add`).

!!! note "Import-Name vs. Installations-Name"
    Sie können sich unterscheiden! `grimm__python__zero` installiert man als
    `pip install grimm-python-zero`, aber du schreibst `from grimm import Actor`.
    Der **Ordner** entscheidet den Import-Namen; der `name` in `pyproject.toml`
    entscheidet den Installations-Namen.

## Bauen, testen, packen

```sh
uv run python -c "from grimm import Actor; print(Actor())"
uv run --with pytest pytest      # deine Tests ausführen
uv build                          # ein installierbares Wheel in dist/ bauen
```

Ein **Test** ist Code, der deinen Code prüft. Er ist zugleich ein Versprechen:
„das funktioniert noch“. Tests grün zu halten, während du Dinge änderst, ist der
Weg, wie echte Projekte vertrauenswürdig bleiben.

```python
# tests/test_actor.py
from grimm import Actor

def test_default_name():
    assert Actor().name() == "Namenloser"
```

## Veröffentlichen

Pakete leben auf [PyPI](https://pypi.org), dem Python Package Index, damit jeder
sie installieren kann:

```sh
uv build       # macht die Dateien in dist/
uv publish     # lädt sie zu PyPI hoch
```

Danach kann die ganze Welt `pip install dein-paket` machen. `grimm-python-zero`
selbst wird genau so veröffentlicht — über einen automatischen Release auf GitHub.

!!! warning "Veröffentlichen ist für immer"
    Eine Version auf PyPI kann nicht neu hochgeladen oder wirklich gelöscht
    werden. Bring es zuerst lokal zum Laufen und frag eine Mentorin, bevor du zum
    ersten Mal wirklich veröffentlichst.

## Probier es

!!! example "Übung — erweitern und beweisen"
    Starte von `grimm__python__zero`. Füge `Actor` eine neue Methode hinzu (z. B.
    `leave_dungeon()`), schreibe einen Test dafür in `tests/` und bring
    `task test` zum Bestehen.

??? tip "Ein Anfangstest"
    ```python
    --8<-- "snippets/11-test-leave.py"
    ```

## Zusammenfassung

- Ein **Paket** = ein Quellordner + `pyproject.toml`.
- `__init__.py` macht den Ordner zum Paket und wählt die Exporte.
- Installations-Name (`pyproject`) und Import-Name (Ordner) können sich
  unterscheiden.
- `uv build` macht es; `uv publish` teilt es auf PyPI — für immer.

---

Du hast das Ende des Anfängerpfads erreicht. Jetzt geh
[ins Verlies](https://github.com/TheGrimmClub/grimm__dungeon__mono). 🕯️
