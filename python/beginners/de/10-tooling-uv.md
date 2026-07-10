# 10 · Werkzeug · uv

> Die moderne Art, Python, Pakete und Projekte zu verwalten — ein schnelles Werkzeug.

## Was du lernst

- Was **uv** ist und warum der Club es nutzt
- Python installieren, ohne mit deinem System zu kämpfen
- Ein Projekt starten und Abhängigkeiten hinzufügen
- Code in der Umgebung des Projekts ausführen

## Die Idee

[uv](https://docs.astral.sh/uv) ersetzt das alte Gewirr aus `pip`, `venv`,
`pyenv` und Co. durch ein einziges schnelles Werkzeug. Es wurde an Tag eins in
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup) installiert.

```sh
uv python install 3.13     # Python selbst holen
uv init grimm-first        # neues Projekt starten (erstellt pyproject.toml)
cd grimm-first
uv add requests            # eine Abhängigkeit hinzufügen, samt Lockfile
uv run main.py             # in der Umgebung des Projekts ausführen
```

Warum Python *über* uv verwalten statt des System-Python?

- macOS liefert ein altes Python für das Betriebssystem — nicht anfassen.
- Linux koppelt Python an Systempakete; ein Upgrade kann Dinge zerbrechen.
- Windows hat standardmäßig gar kein Python.

uv gibt jedem Club-Mitglied **denselben** Interpreter, isoliert und
reproduzierbar.

## Probier es

!!! example "Übung"
    1. `uv init grimm-first && cd grimm-first`
    2. `uv run main.py`
    3. `uv add rich`, dann in `main.py`: `from rich import print` und gib etwas
       Farbiges aus.

## Spickzettel

| Befehl | Tut |
|--------|-----|
| `uv python install 3.13` | eine Python-Version installieren |
| `uv init NAME` | ein Projekt starten |
| `uv add PKG` | eine Abhängigkeit hinzufügen |
| `uv run DATEI` | in der Projektumgebung ausführen |
| `uv sync` | alles aus dem Lockfile installieren |

---

**Weiter:** [11 · Baue dein Paket](11-create-your-package.md).
