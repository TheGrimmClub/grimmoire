# Einrichtung 2 · Python installieren

> Die Sprache selbst — von uv installiert, damit sie dir gehört und nicht deinem Betriebssystem.

Du hast den Zauberstab. Jetzt die Magie, die er leitet.

Python ist ein Programm wie jedes andere, und vielleicht hast du schon eins auf
dem Rechner. Wir installieren trotzdem unser eigenes, und in diesem Kapitel geht
es auch darum, *warum* das keine Verschwendung ist.

## Was du lernst

- Warum der Club nicht das Python nutzt, das mitgeliefert wurde
- Python mit einem uv-Befehl installieren
- Prüfen, welche Version du bekommen hast
- Warum `uv run` die Frage „welches Python?" verschwinden lässt

## Warum nicht das Python, das du schon hast

Tipp das — es antwortet vielleicht, vielleicht auch nicht:

```sh
uv run python --version
```

So oder so: Der Club installiert sein eigenes. Die Gründe unterscheiden sich je
nach System:

- **macOS** liefert ein altes Python mit, das das Betriebssystem selbst benutzt.
  Änderst du es, kannst du Teile von macOS kaputt machen. Lass es in Ruhe.
- **Linux** koppelt Python an Systempakete, ein Upgrade kann also Dinge
  deinstallieren, die du gebraucht hast.
- **Windows** hat meist gar kein Python, bis du eins hinzufügst.

!!! note "Der eigentliche Grund: alle gleich"
    Eine gemeinsame Werkbank funktioniert nur, wenn die Werkzeuge
    zusammenpassen. Wenn jeder Lehrling denselben Interpreter benutzt, ist „bei
    mir läuft's" kein Argument mehr, und Code, der bei dir läuft, läuft auch bei
    der Person neben dir.

## Die Installation

```sh
uv python install 3.13
```

Das lädt Python 3.13 herunter und legt es in uvs eigenen Speicher — nicht
vermischt mit deinem System.

Um zu sehen, was du hast:

```sh
uv python list
```

Du bekommst eine Liste von Versionen, die installierten sind markiert. Mehrere
Einträge sind normal und kein Grund zur Sorge.

## Welches Python läuft?

```sh
uv run python --version
```

```
Python 3.13.0
```

`uv run` ist die wichtige Hälfte dieses Befehls: Es wählt das richtige Python
für den Ort, an dem du bist — statt irgendeines, das die Shell zuerst findet. Ab
hier führt das Buch Python immer über `uv run` aus, damit du dich nie fragen
musst, welcher Interpreter geantwortet hat.

!!! tip "Eine andere Nummer?"
    Alles ab `3.13` ist für dieses Buch in Ordnung. Wenn du `3.9` oder ähnliches
    siehst, antwortet dir ein System-Python — prüfe, ob
    `uv python install 3.13` ohne Fehler durchgelaufen ist.

## Zusammenfassung

- Das System-Python gehört deinem **Betriebssystem**; lass es in Ruhe.
- `uv python install 3.13` gibt dir eins, das **dir** gehört.
- `uv run python` wählt immer das richtige.

## Spickzettel

| Du willst… | Befehl |
|------------|--------|
| Python 3.13 installieren | `uv python install 3.13` |
| Installierte Versionen sehen | `uv python list` |
| Prüfen, welches läuft | `uv run python --version` |

---

**Weiter:** [Einrichtung 3 · Installation testen](a__03-test-installation.md) — beweisen, dass alles läuft.
