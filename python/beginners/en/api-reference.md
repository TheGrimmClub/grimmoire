# grimm · API Reference

Reference for the [`grimm`](https://github.com/TheGrimmClub/grimm__python__zero)
package — the day-two package you build, and the bridge to the dungeon. Three
public classes:

| Class | What it is |
|-------|------------|
| [`Actor`](#actor) | your first Python class — a character in the Grimm world |
| [`Dungeon`](#dungeon) | a launcher/on-ramp to the real `grimm__dungeon__mono` adventure |
| [`Game`](#game) | a read **and write** view of the dungeon's saved game |

```python
from grimm import Actor, Dungeon, Game
```

The package is **dependency-free** and targets **Python ≥ 3.9**.

---

## Actor

`grimm.actor.Actor` — a character (a player's avatar). The teaching class of the
beginner path (see [09 · Classes](09-classes.md)).

### Constructor

```python
Actor(name="Namenloser")
```

| Param | Type | Default | Meaning |
|-------|------|---------|---------|
| `name` | `str` | `"Namenloser"` (constant `DEFAULT_NAME`) | the actor's name |

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `name()` | `str` | the actor's name |
| `enter_dungeon(launch=False)` | `int \| None` | tell the story; with `launch=True`, hand off to `Dungeon().enter()` and return its exit code |
| `__str__()` | `str` | what `print(actor)` shows — `🧍 Hans wartet vor dem Verlies.` (changes to `… im Verlies.` after entering) |
| `__repr__()` | `str` | developer view — `Actor(name='Hans')` |

```python
me = Actor(name="Hans")
print(me.name())          # Hans
print(me)                 # 🧍 Hans wartet vor dem Verlies.
me.enter_dungeon()        # Hans betritt das Verlies. … 🕯️
```

---

## Dungeon

`grimm.dungeon.Dungeon` — finds (or **builds**) the `grimm` console program from
`grimm__dungeon__mono`, seeds the work dir with the package, and launches it.

### Constructor

```python
Dungeon(executable=None, source=None)
```

| Param | Type | Default | Meaning |
|-------|------|---------|---------|
| `executable` | `str \| Path \| None` | `None` | explicit path to a prebuilt `grimm` binary |
| `source` | `str \| Path \| None` | `None` | explicit path to a checkout to build |

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `find()` | `Path \| None` | a ready-to-run binary: `executable`/`GRIMM_BIN`, then `PATH`, then a nearby checkout's `bin/grimm` |
| `find_source()` | `Path \| None` | a buildable checkout nearby (has `go.mod` + `cmd/grimm`) |
| `build()` | `Path \| None` | build from source (`task build`, else `go build`); the binary path or `None` |
| `home()` *(static)* | `Path` | `~/.grimm` |
| `workspace()` | `Path` | `~/.grimm/work` (created on demand) |
| `seed_workspace()` | `Path` | write the `grimm` (Actor) package into `~/.grimm/work/grimm/`; idempotent |
| `game()` | [`Game`](#game) `\| None` | the saved game, or `None` |
| `world_names()` | `dict[str, str]` | map ids → human names from a nearby checkout (`helm` → `"Helm mit Stirnlampe"`) |
| `show()` | `Game \| None` | print a summary of the saved game (with names); returns it |
| `status()` | `dict` | `{binary, source, workspace, buildable}` |
| `enter(build=True)` | `int` | resolve/build the binary, seed the work dir, set `GRIMM_BIN`, launch; grimm's exit code (or `1`) |

```python
from grimm import Dungeon

Dungeon().enter()          # find or build, then play
Dungeon().show()           # inventory, room, progress — with names
Dungeon().status()         # {'binary': …, 'source': …, 'workspace': …, 'buildable': False}
```

### Constants & environment
- `grimm.dungeon.EXECUTABLE` — `"grimm"` (`"grimm.exe"` on Windows).
- `grimm.dungeon.CHECKOUT` — `"grimm__dungeon__mono"`.
- **`GRIMM_BIN`** — if set, `find()` uses it first; `enter()` sets it for the child.

---

## Game

`grimm.game.Game` — a read/write view of the dungeon's save,
`~/.grimm/save.syon`. A tiny purpose-built SYON reader/emitter keeps the package
dependency-free and the output exactly what the Go game reads.

### Constructor

```python
Game(path=None)   # loads ~/.grimm/save.syon automatically, if it exists
```

### Attributes (loaded on construction)

| Attribute | Type | Meaning |
|-----------|------|---------|
| `version` | `int` | save format version (`1`) |
| `title` | `str` | player's class (e.g. `"Jäger"`) |
| `location` | `str` | current room id |
| `inventory` | `list[str]` | item ids carried |
| `worn` | `list[str]` | item ids worn |
| `visited` | `list[str]` | room ids seen |
| `solved` | `list[str]` | puzzle ids cleared |

### Reading

| Method | Returns | Description |
|--------|---------|-------------|
| `default_path()` *(static)* | `Path` | `~/.grimm/save.syon` |
| `exists()` | `bool` | whether a save file is present |
| `load()` | `Game` | (re)read & parse; returns `self` (raises `FileNotFoundError` if none) |
| `summary(names=None)` | `str` | a human-readable report; pass `Dungeon().world_names()` for full names |
| `actor()` | [`Actor`](#actor) | an actor named after this game's class |

### Writing

All mutators **return `self`** (chainable) and skip duplicates; `write()` persists.

| Method | Description |
|--------|-------------|
| `grant(*items)` | add item ids to the inventory |
| `drop(*items)` | remove item ids (and from `worn`) |
| `wear(item)` | wear an item (granting it first) |
| `visit(*rooms)` | mark room ids visited |
| `solve(*puzzles)` | mark puzzle ids solved |
| `go(room)` | set the current room |
| `write(path=None)` | write SYON the dungeon can load; returns the path |

```python
game = Game()
game.grant("zeitsiegel").wear("helm").visit("archiv").solve("repo-tor").go("halle")
game.write()   # ~/.grimm/save.syon — verified to load in the Go game's state.Load
```

!!! warning "Save version"
    `write()` overwrites the whole save with the known v1 fields. If a future
    dungeon adds fields, bump the writer to match.

---

## Save file format

`~/.grimm/save.syon` — SYON (safe YAML), written by `grimm__dungeon__mono` (Go,
native SYON parser) and by `Game.write()`:

```yaml
version: 1
game:
  title: Jäger
  location: archiv
  inventory:
    - helm
    - nanostaub
  worn:
    - helm
  visited:
    - archiv
    - tor
  solved:
    - repo-tor
```

Empty lists are a bare `inventory:` (SYON has no `[]` flow). Ids (rooms, items,
puzzles) come from the world content in `grimm__dungeon__mono/content/world/*.syon`.

---

## How it fits together

```
grimmoire (learn)            grimm__python__zero (build)       grimm__dungeon__mono (play)
─────────────────            ──────────────────────────       ───────────────────────────
Actor / Dungeon / Game     → from grimm import Actor        → puzzles run python3 loesung.py
                             Dungeon().enter() ─────────────→   (work dir seeded → import Actor)
Dungeon().show()  ←───────── reads  ~/.grimm/save.syon  ←────  the game writes progress
Game().grant(...).write()   → writes ~/.grimm/save.syon ────→  state.Load reads it back
```

- **Learn** the concepts here in the Grimmoire.
- **Build** the `grimm` package ([11 · Create Your Package](11-create-your-package.md)).
- **Play**: `Dungeon().enter()` launches the adventure; the
  [Lernpfad](https://github.com/TheGrimmClub/grimm__dungeon__mono) puzzles use your Python.
- **Read/write** your progress with `Dungeon`/`Game`.

Runnable examples live in the package: `examples/step1.py … step4.py`
(`task step1`, `task step2`, `task dungeon`, `task save`).
