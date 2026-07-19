# GRIMMoire

*The Grimm Club spell book — a beginner Python path, in two tongues.*

The spell book, directly usable by [micro](https://micro-editor.github.io) via
its help system, and published as a site.

📖 **[thegrimmclub.github.io/grimmoire](https://thegrimmclub.github.io/grimmoire)**

## The Python Beginner Path

From your first command in a shell to your own published package — in English
and German.

| | |
|---|---|
| **English** | [Start the path](python/beginners/en/index.md) · [Manifesto](python/beginners/en/00-manifest.md) |
| **Deutsch** | [Zum Lernpfad](python/beginners/de/index.md) · [Manifest](python/beginners/de/00-manifest.md) |

**Setup** — do this once: [install uv](python/beginners/en/a__01-setup-uv.md) →
[install Python](python/beginners/en/a__02-setup-python.md) →
[test it](python/beginners/en/a__03-test-installation.md).

**The eleven stages** — commands & calls, imports, argparse, variables &
values, the debugger, conditions, loops, functions, classes, tooling with uv,
and finally creating your own package.

Solution code is single-sourced from `python/beginners/snippets/*.py` and pulled
into both languages at build time, so the two never drift apart.

## Building the site

The site is built with [Zensical](https://zensical.org). Everything runs through
[uv](https://docs.astral.sh/uv) — the same tool the curriculum teaches — so the
version in `uv.lock` is what you and GitHub Actions both get.

```sh
uv run zensical serve     # live-reload preview at localhost:8000
uv run zensical build     # build into site/
```

Or through [Task](https://taskfile.dev), the front door in every Grimm Club
repository:

```sh
task docs:serve
task docs:build
```

Pushing to `main` builds and publishes to GitHub Pages automatically — see
[.github/workflows/deploy.yml](.github/workflows/deploy.yml).

## Beyond the book

- Day-one setup: [GrimmSetup](https://github.com/TheGrimmClub/GrimmSetup)
- The package you build on day two:
  [grimm__python__zero](https://github.com/TheGrimmClub/grimm__python__zero)
- The adventure that ties it together:
  [GrimmDungeon](https://github.com/TheGrimmClub/grimm__dungeon__mono)
