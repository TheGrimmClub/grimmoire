# 11 · Baue dein Paket

> Veröffentliche etwas Echtes: mach aus deinem Code ein Paket, das andere installieren können.

## Was du lernst

- Die Form eines Python-Pakets (`pyproject.toml` + ein Quellordner)
- Wie `from deinpaket import Ding` funktioniert
- Tests hinzufügen
- Was „veröffentlichen“ bedeutet

## Die Idee

Ein **Paket** ist ein Ordner voller Module plus eine `pyproject.toml`, die es
beschreibt. Du hast schon eins gesehen:
[grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero).

```
grimm-first/
├── pyproject.toml      # Name, Version, nötiges Python, Abhängigkeiten
├── grimm/              # das Paket (importierbar als `grimm`)
│   ├── __init__.py     # Re-Exports: from grimm import Actor
│   └── actor.py        # dein Code
└── tests/
    └── test_actor.py   # Beweis, dass es funktioniert
```

Eine minimale `pyproject.toml`:

```toml
[project]
name = "grimm-first"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Dann:

```sh
uv run python -c "from grimm import Actor; print(Actor())"
uv run --with pytest pytest      # deine Tests ausführen
uv build                          # ein Wheel bauen, das du veröffentlichen könntest
```

## Probier es

!!! example "Übung"
    Starte von `grimm__python__zero`, füge `Actor` eine neue Methode hinzu,
    schreibe einen Test dafür in `tests/` und bring `task test` zum Bestehen.

!!! tip "Veröffentlichen"
    Pakete leben auf [PyPI](https://pypi.org), damit jeder sie per
    `pip install` holen kann. `uv build` macht die Datei; `uv publish` lädt sie
    hoch. Frag eine Mentorin, bevor du zum ersten Mal wirklich veröffentlichst.

---

Du hast das Ende des Anfängerpfads erreicht. Jetzt geh
[ins Verlies](https://github.com/TheGrimmClub/grimm__dungeon__mono). 🕯️
