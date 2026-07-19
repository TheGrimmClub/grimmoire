# Einrichtung 1 · uv installieren

> Vor dem ersten Zauber der Zauberstab: `uv` auf deinen Rechner bringen.

Jeder Lehrling braucht eine Werkbank, bevor er ein Zauberbuch braucht. Dieses
kurze Einrichtungskapitel macht deinen Rechner bereit — ein Werkzeug, dann
Python selbst, dann ein Test, der beweist, dass alles läuft.

Das machst du nur einmal. Wenn du an Tag eins dabei warst und
[GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup) durchgearbeitet hast,
ist das schon erledigt und du kannst direkt zu
[01 · Befehle & Aufrufe](01-commands-and-calls.md) springen.

## Was du lernst

- Was **uv** ist, in einem Satz
- Wie man es auf macOS, Linux oder Windows installiert
- Wie du prüfst, ob die Installation geklappt hat
- Was zu tun ist, wenn die Shell `command not found` sagt

## Was uv ist

`uv` ist ein einziges, sehr schnelles Werkzeug, das Python für dich verwaltet —
den Interpreter, die Bibliotheken und deine Projekte. Es ersetzt das alte
Gestrüpp aus `pip`, `venv` und `pyenv`.

Für den Moment reicht dieser eine Satz. Was es wirklich kann, lernst du in
[10 · Werkzeug · uv](10-tooling-uv.md); hier brauchen wir es nur installiert.

## Die Installation

Öffne deine Shell und führe die Zeile für dein System aus.

Auf **macOS oder Linux**:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Auf **Windows**, in der PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

!!! note "Einen Befehl lesen, bevor du ihn ausführst"
    Ein Skript aus dem Internet in die Shell zu leiten ist bei
    Entwickler-Werkzeugen üblich, aber es lohnt sich zu wissen, was du gerade
    getan hast: Es hat Astrals Installationsskript geladen und ausgeführt. Du
    kannst es vorher lesen, indem du
    [astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) im Browser
    öffnest. Ein guter Lehrling schaut in den Kessel, bevor er trinkt.

## Prüfen, ob es geklappt hat

Schließe deine Shell und öffne eine **neue** — Installationsprogramme ändern
deinen `PATH`, und eine alte Shell hat das nicht mitbekommen.

```sh
uv --version
```

```
uv 0.9.29
```

Deine Nummer wird anders sein, und das ist in Ordnung. Irgendeine Antwort
bedeutet: uv ist da.

!!! tip "`command not found: uv`"
    Die Installation hat geklappt, aber deine Shell sieht uv noch nicht. Der
    Reihe nach:

    1. Öffne ein ganz neues Shell-Fenster — der übliche Fix.
    2. Starte die Terminal-App komplett neu.
    3. Immer noch nichts? Das Installationsprogramm hat eine Zeile ausgegeben,
       welche Datei du für deinen `PATH` anpassen musst. Scrolle zurück und lies
       sie — die Antwort steht in der Ausgabe.

## Zusammenfassung

- **uv** ist das eine Werkzeug für Python, Pakete und Projekte.
- Installation mit einem Befehl, danach eine **neue** Shell öffnen.
- Wenn `uv --version` irgendetwas antwortet, bist du bereit.

## Spickzettel

| Du willst… | Befehl |
|------------|--------|
| uv installieren (macOS/Linux) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| uv installieren (Windows) | `irm https://astral.sh/uv/install.ps1 \| iex` |
| Prüfen, ob uv da ist | `uv --version` |

---

**Weiter:** [Einrichtung 2 · Python installieren](a__02-setup-python.md) — die Sprache selbst.
