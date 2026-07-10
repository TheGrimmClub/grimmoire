# 03 · argparse

> Let your program take orders: reading arguments from the command line.

## What you'll learn

- The difference between `sys.argv` and `argparse`
- How to define an argument with a name, type, and help text
- How to run a script with options

## The idea

Programs become useful when the user can steer them. The raw way is `sys.argv`
(a list of the words typed after `python`):

```python
import sys
print(sys.argv)   # ['script.py', 'Nord', '--loud']
```

`argparse` does the tedious parsing for you and gives free `--help`:

```python
import argparse

parser = argparse.ArgumentParser(description="Greet a Grimm hero.")
parser.add_argument("name", help="the hero's name")
parser.add_argument("--shout", action="store_true", help="use capitals")
args = parser.parse_args()

greeting = f"Hallo {args.name}"
print(greeting.upper() if args.shout else greeting)
```

```sh
python greet.py Hänsel --shout   # HALLO HÄNSEL
python greet.py --help           # argparse prints usage for free
```

## Try it

!!! example "Übung"
    Write `enter.py` that takes a `name` argument and prints
    `f"{name} betritt das Verlies."` Add an optional `--torch` flag that also
    prints `🕯️`.

## Cheat sheet

| Piece | Does |
|-------|------|
| `add_argument("name")` | a required positional value |
| `add_argument("--flag", action="store_true")` | an on/off switch |
| `add_argument("--n", type=int)` | convert to a number |
| `parse_args()` | read the actual command line |

---

**Next:** [04 · Variables & Values](04-variables-and-values.md).
