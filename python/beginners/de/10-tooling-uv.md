# 10 · Werkzeug · uv

> Die moderne Art, Python, Pakete und Projekte zu verwalten — ein schnelles Werkzeug.

Bisher hast du einzelne Dateien ausgeführt. Echte Projekte brauchen mehr: die
richtige Python-Version, zusätzliche Bibliotheken und einen Weg, alles
reproduzierbar zu halten, damit es auf *jedermanns* Maschine läuft. Genau dafür
ist [uv](https://docs.astral.sh/uv) da.

## Was du lernst

- Was **uv** ist und warum der Club es nutzt
- Python installieren, ohne mit deinem System zu kämpfen
- Ein Projekt starten und Abhängigkeiten hinzufügen
- Code in der Umgebung des Projekts ausführen

## Was uv ist

`uv` ist ein einziges, sehr schnelles Werkzeug (in Rust geschrieben), das das
alte Gewirr aus `pip`, `venv`, `pyenv` und Co. ersetzt. Es wurde an Tag eins in
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup) installiert.

```sh
uv --version
```

## Python selbst verwalten

uv kann Python für dich installieren — kein System-Chaos:

```sh
uv python install 3.13     # Python 3.13 herunterladen und installieren
uv python list             # sehen, was installiert ist
```

!!! note "Warum nicht das System-Python?"
    - macOS liefert ein altes Python für das Betriebssystem — nicht anfassen.
    - Linux koppelt Python an Systempakete; ein Upgrade kann Dinge zerbrechen.
    - Windows hat standardmäßig gar kein Python.

    uv gibt jedem Club-Mitglied **denselben** Interpreter, isoliert und
    reproduzierbar.

## Ein Projekt in vier Befehlen

```sh
uv init grimm-first     # 1. ein Projekt anlegen (erstellt pyproject.toml + main.py)
cd grimm-first
uv add rich             # 2. eine Abhängigkeit hinzufügen (samt Lockfile)
uv run main.py          # 3. in der eigenen Umgebung des Projekts ausführen
uv sync                 # 4. alles aus dem Lockfile (neu) installieren
```

`uv run` ist der magische Befehl: er stellt sicher, dass die Umgebung bereit ist,
und führt dann deinen Code mit genau dem richtigen Python und den richtigen
Bibliotheken aus — keine „läuft nur bei mir“-Überraschungen.

!!! tip "Das Lockfile"
    `uv add` schreibt ein genaues Rezept (`uv.lock`) jedes Pakets und jeder
    Version. Committe es, und das `uv sync` einer Kollegin stellt deine Umgebung
    Byte für Byte wieder her.

## Ausführliches Beispiel

```sh
uv init grimm-first
cd grimm-first
uv add rich
```

Schreibe das in `main.py`:

```python
from rich import print

print("[bold magenta]Willkommen im Grimm Club![/]")
```

Führe es aus:

```sh
uv run main.py
```

Du hast gerade eine Fremdbibliothek benutzt, von uv installiert und verdrahtet,
mit Farbe in deinem Terminal.

## Probier es

!!! example "Übung — ein farbiger Held"
    Führe in deinem `grimm-first`-Projekt `uv add rich` aus und gib dann den Namen
    deines Helden in einer Farbe deiner Wahl aus, mit `from rich import print` und
    `[farbe]...[/]`.

??? tip "Tipp"
    ```python
    from rich import print
    print("[green]Hänsel[/] betritt den Wald.")
    ```

## Zusammenfassung

- **uv** verwaltet Python-Versionen, Abhängigkeiten und Umgebungen — ein Werkzeug.
- Installiere Python *über* uv, nicht über das System, für dieselbe Einrichtung
  überall.
- `uv init` → `uv add` → `uv run` → `uv sync` ist die alltägliche Schleife.

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
