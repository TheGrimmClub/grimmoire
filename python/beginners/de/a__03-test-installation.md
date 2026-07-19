# Einrichtung 3 · Installation testen

> Beweisen, dass die Werkbank funktioniert — ein echtes Projekt, eine echte Datei, ein echter Lauf.

Zwei Befehle haben dir höflich geantwortet. Das ist noch kein Beweis. In diesem
Kapitel baust du etwas Kleines und führst es aus, damit du Kapitel 01 beginnst
und *weißt*, dass deine Werkzeuge laufen — statt es zu hoffen.

## Was du lernst

- Dein erstes Projekt mit `uv init` anlegen
- Eine Datei schreiben und mit `uv run` ausführen
- Eine Fehlermeldung lesen, statt sie zu fürchten
- Die drei Dinge, die am ersten Tag schiefgehen

## Ein Projekt anlegen

```sh
uv init grimm-first
cd grimm-first
```

`uv init` legt einen Ordner mit ein paar Dateien an. Zwei sind heute wichtig:

- `pyproject.toml` — die Visitenkarte des Projekts. Sie sagt, was dieses Projekt
  ist und was es braucht.
- `main.py` — eine Python-Startdatei, mit einem `print(...)` schon darin.

Den Rest lernst du in [10 · Werkzeug · uv](10-tooling-uv.md) kennen und baust
eins richtig in [11 · Baue dein Paket](11-create-your-package.md).

## Ausführen

```sh
uv run main.py
```

```
Hello from grimm-first!
```

Diese Ausgabe ist der ganze Sinn des Einrichtungskapitels. Python ist
installiert, das Projekt ist echt, und `uv run` hat beides verbunden.

!!! note "Was `uv run` gerade getan hat"
    Es hat geprüft, ob das Projekt eine Umgebung hat, eine angelegt falls nicht,
    und dann deine Datei darin ausgeführt. Deshalb musstest du nie etwas
    „aktivieren".

## Schreib dein eigenes

Öffne `main.py` in deinem Editor — [micro](https://micro-editor.github.io), wenn
du GrimmSetup gefolgt bist — und ersetze den Inhalt durch:

```python
print("Der Wald ist dunkel, aber der Pfad ist erhellt.")
```

```sh
uv run main.py
```

```
Der Wald ist dunkel, aber der Pfad ist erhellt.
```

Du hast gerade dein eigenes Python geschrieben und ausgeführt. Alles Weitere ist
Detail.

## Wenn es schiefgeht

Das wird es, und das ist ganz normal. Die drei von Tag eins:

**`command not found: uv`** — die Shell sieht uv nicht. Öffne ein neues Fenster;
siehe [Einrichtung 1](a__01-setup-uv.md).

**`No such file or directory: main.py`** — du bist im falschen Ordner. Frag mit
`pwd`, wo du bist, und mit `ls`, was dort liegt. Du musst *innerhalb* von
`grimm-first` sein.

**`SyntaxError`** — ein Tippfehler im Python selbst. Fast immer ein fehlendes
Anführungszeichen oder eine fehlende Klammer. Python gibt die Zeilennummer aus
und zeigt mit einem `^` auf die Stelle:

```
  File "main.py", line 1
    print("Der Wald ist dunkel)
          ^
SyntaxError: unterminated string literal
```

!!! tip "Fehler sind Wegweiser, keine Urteile"
    Eine Fehlermeldung ist Python, das dir genau sagt, wo es nicht mehr
    weiterwusste. Lies sie **von unten nach oben**: Die letzte Zeile sagt, *was*
    schiefging, die Zeilen darüber sagen *wo*. Das ist eine Fähigkeit, und du
    fängst jetzt an, sie aufzubauen — richtig schärfen wirst du sie in
    [05 · Debugger](05-debugger.md).

## Zusammenfassung

- `uv init <name>` startet ein Projekt; `uv run <datei>` führt Code darin aus.
- `pyproject.toml` ist die Visitenkarte des Projekts.
- Fehler nennen Datei, Zeile und Problem — lies sie von unten nach oben.

## Spickzettel

| Du willst… | Befehl |
|------------|--------|
| Ein Projekt starten | `uv init grimm-first` |
| Eine Datei ausführen | `uv run main.py` |
| Wo bin ich? | `pwd` |
| Was ist hier? | `ls` |

---

Die Werkbank steht. Zeit für den ersten Zauber.

**Weiter:** [01 · Befehle & Aufrufe](01-commands-and-calls.md) — mit der Maschine sprechen.
