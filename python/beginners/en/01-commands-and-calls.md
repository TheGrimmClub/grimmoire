# 01 · Commands & Calls

> Talking to the machine: typing commands in the shell, and calling functions in Python.

## What you'll learn

- What a **shell** is and how to run a command
- How to start Python and run a `.py` file
- What a **function call** looks like — `name(arguments)`
- Your first call: `print(...)`

## The idea

A **command** is an instruction you type into the shell (your terminal). A
**call** is when you tell a piece of code to run — you say its name and hand it
some values in parentheses.

```python
print("Hallo, Grimm Club!")
```

`print` is the function. `"Hallo, Grimm Club!"` is the **argument** you pass to
it. The parentheses mean "do it now".

In the shell you do the same thing with programs:

```sh
python hello.py        # run a Python file
python -c "print(2+2)" # run one line of Python
```

## Try it

!!! example "Übung"
    1. Open your terminal (the [micro](https://micro-editor.github.io) editor and
       a shell were set up in **GrimmSetup**).
    2. Type `python -c "print('mein Name')"` — replace it with your name.
    3. Make a file `hello.py` with one `print(...)` line and run it with
       `python hello.py`.

## Cheat sheet

| You want to… | Command |
|--------------|---------|
| Run a Python file | `python file.py` |
| Run one line | `python -c "..."` |
| Print something | `print(value)` |
| Quit the Python shell | `exit()` |

---

**Next:** [02 · Imports](02-imports.md) — using code other people wrote.
