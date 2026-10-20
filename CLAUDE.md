# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A small Python teaching app for the Scouts BSA Programming merit badge. It models a zoo of animals to demonstrate classes, inheritance and method overriding. Standard library only; no build, lint or test tooling is set up yet.

## Commands

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Architecture

- `animal.py`: `Animal` base class. Holds `name` and defines `move()` and `animal_type()`; subclasses override these.
- `menagerie.py`: all concrete `Animal` subclasses (`Giraffe`, `Lion`, `Elephant`, `Panda`). New animals go here. `zoo.py` and `main.py` pull them in with `from menagerie import *`.
- `zoo.py`: `Zoo` stores a count per species (`dict` keyed by `animal.animal_type()`), not the animal objects themselves. `print_roster()` prints the counts and a total.
- `main.py`: script that builds a `Zoo`, adds some animals and prints the roster.

Because `Zoo` groups by `animal_type()`, every subclass needs an `animal_type()` override that returns its own class name. Otherwise it gets counted under the wrong species.

## Intentional bugs (do not fix)

This code is a tutorial, and a Scout is meant to find and fix these bugs. Leave them in place and don't hint at them unprompted, unless the user explicitly asks for the fix:

- `Lion.animal_type()` returns `'Giraffe'`.
- `Panda` has no `animal_type()` override, so it is counted as `'Animal'`.

## Project skills

- `.claude/skills/create-animal`: adds a new `Animal` subclass to `menagerie.py`, named for the animal, with an `animal_type()` override that returns the class name.
