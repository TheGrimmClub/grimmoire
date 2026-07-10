# 03 · argparse

> Let your program take orders: reading arguments from the command line.

A program gets useful when the person running it can steer it — the same way you
steered the shell in [chapter 01](01-commands-and-calls.md). `argparse` turns the
words after `python yourscript.py` into neat, named values.

## What you'll learn

- The difference between `sys.argv` and `argparse`
- Defining an argument with a name, type, and help text
- Positional arguments vs. `--options`
- The free `--help` you get for nothing

## The raw way: `sys.argv`

Everything typed after `python` lands in a list called `sys.argv`:

```python
import sys
print(sys.argv)     # ['greet.py', 'Nord', '--loud']
```

`sys.argv[0]` is the script name; the rest are what the user typed. It works, but
*you* have to figure out what each word means. That gets messy fast.

## The good way: `argparse`

`argparse` parses the command line for you and even writes the help text:

```python
import argparse

parser = argparse.ArgumentParser(description="Greet a Grimm hero.")
parser.add_argument("name", help="the hero's name")
parser.add_argument("--shout", action="store_true", help="use capitals")
args = parser.parse_args()

greeting = f"Hallo {args.name}"
print(greeting.upper() if args.shout else greeting)
```

Run it:

```sh
python greet.py Hänsel            # Hallo Hänsel
python greet.py Hänsel --shout    # HALLO HÄNSEL
python greet.py --help            # usage text, written for you
```

## Positional vs. optional

- **Positional** (`"name"`) — required, identified by *where* it sits.
- **Optional** (`"--shout"`) — starts with `--`, identified by *name*, usually
  optional.

Two handy kinds of optional argument:

```python
parser.add_argument("--shout", action="store_true")  # a flag: on/off
parser.add_argument("--hp", type=int, default=100)    # a value, converted to int
```

`action="store_true"` makes a switch that's `False` unless the user adds it.
`type=int` converts the text `"25"` into the number `25`.

!!! tip "You get --help free"
    Because you described each argument, `python greet.py --help` prints a full
    usage message. Good tools explain themselves.

## Try it

!!! example "Übung — enter the dungeon"
    Write `enter.py` that takes a positional `name` and prints
    `f"{name} betritt das Verlies."` Add an optional `--torch` flag that also
    prints `🕯️`.

??? tip "Solution"
    <!-- snippet: 03-enter.py -->
    ```python
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--torch", action="store_true")
    args = parser.parse_args()

    print(f"{args.name} betritt das Verlies.")
    if args.torch:
        print("🕯️")
    ```
    <!-- endsnippet -->
    ```sh
    python enter.py Gretel --torch
    ```

## Recap

- `sys.argv` is the raw list; `argparse` turns it into named values.
- **Positional** args are required by position; **`--options`** are named.
- `action="store_true"` = a flag; `type=int` converts text to a number.
- You get `--help` for free.

## Cheat sheet

| Piece | Does |
|-------|------|
| `add_argument("name")` | a required positional value |
| `add_argument("--flag", action="store_true")` | an on/off switch |
| `add_argument("--n", type=int)` | convert to a number |
| `parse_args()` | read the actual command line |

---

**Next:** [04 · Variables & Values](04-variables-and-values.md).
