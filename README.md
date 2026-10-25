# 42 Python Module 05bis — The Codex

**Packages, Environments and the Alchemist's Toolchain**

A collection of exercises for the 42 curriculum covering Python virtual environments, dependency management, environment-based configuration, modules, packages, import mechanisms, and circular dependencies.

## Requirements

- Python **3.10 or newer**
- `pip` and `venv` for the first exercise
- [Poetry](https://python-poetry.org/) (optional alternative dependency manager in Exercise 0)
- `flake8` and `mypy` for code checks

Exercises 0 and 1 use third-party libraries. Exercises 2–4 rely on the standard library and modules in this repository.

## Project structure

```text
.
├── ex0/
│   ├── construct.py
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
├── ex1/
│   ├── .env.example
│   ├── .gitignore
│   ├── oracle.py
│   └── requirements.txt
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── transmutation/
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── grimoire/
│       ├── __init__.py
│       ├── light_spellbook.py
│       ├── light_validator.py
│       ├── dark_spellbook.py
│       └── dark_validator.py
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_distillation_0.py
├── ft_transmutation_0.py
├── ft_kaboom_0.py
└── ft_kaboom_1.py
```

## Exercise 0 — The Sealed Laboratory

Learn how virtual environments isolate installed Python packages and how to manage dependencies with **pip** and **Poetry**.

### Part 1: Virtual environment detection

Run this from the repository root, outside a virtual environment:

```bash
python3 ex0/construct.py
```

Create a virtual environment and try again:

```bash
python3 -m venv lab_env
source lab_env/bin/activate
python3 ex0/construct.py
deactivate
```

`construct.py` displays the current Python interpreter, detects an active virtual environment, and reports the package installation path when inside one.

### Part 2: Dependency management

Install the required packages using **pip**:

```bash
python3 -m venv lab_env
source lab_env/bin/activate
python3 -m pip install -r ex0/requirements.txt
python3 ex0/loading.py
deactivate
```

Alternatively, install and run with **Poetry**:

```bash
cd ex0
poetry install
poetry run python loading.py
cd ..
```

The Poetry configuration uses `package-mode = false` because this exercise manages dependencies for scripts rather than installing a Python package.

`loading.py` checks whether `pandas` and `numpy` are available, prints installed versions, and provides installation hints when an import fails.

## Exercise 1 — The Oracle

Configure a Python program using environment variables and the `python-dotenv` library. Demonstrate how development and production settings differ without embedding secrets in source code.

Install dependencies in a separate virtual environment:

```bash
cd ex1
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Create a local configuration file from the example:

```bash
cp .env.example .env
```

Edit `.env` with your own local configuration, then run:

```bash
python3 oracle.py
```

You can override variables directly in the shell:

```bash
MATRIX_MODE=production API_KEY=example_key python3 oracle.py
```

`load_dotenv()` reads values from `.env`, but **does not overwrite variables already present in the process environment by default**. The script can also run without a `.env` file, using environment variables or fallback values and warnings.

**Security:** `.env` is ignored by Git. Commit `.env.example` with placeholder values only; never commit real API keys or passwords. A `.env` file is not encrypted.

## Exercise 2 — The Alembic

Explore modules, package initialization (`__init__.py`), and which attributes a package exposes.

Run from the repository root:

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
```

- `ft_alembic_0.py` imports the top-level `elements` module and creates fire.
- `ft_alembic_1.py` imports the `alchemy` package, creates air, and then intentionally tries to access `alchemy.create_earth()`.

**Expected failure:** `ft_alembic_1.py` intentionally raises `AttributeError` for the unexposed `create_earth` attribute. The function still exists in `alchemy.elements`.

## Exercise 3 — Distillation and Transmutation

Practice imports across packages and subpackages, including **absolute** and **relative** imports.

```bash
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
```

- `ft_distillation_0.py` imports the potion functions and combines elements from both the root module and the `alchemy` package.
- `ft_transmutation_0.py` calls a recipe from the nested `alchemy.transmutation.recipes` module.

## Exercise 4 — Avoid the Explosion

Compare a working approach to mutually dependent modules with a deliberately broken **circular import**.

```bash
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

- **Light grimoire:** `light_spellbook.py` and `light_validator.py` cooperate successfully. The validator imports the spellbook inside its function, avoiding the problematic initialization-time import cycle.
- **Dark grimoire:** `dark_spellbook.py` and `dark_validator.py` import each other at module scope. This is deliberately broken.

**Expected failure:** `ft_kaboom_1.py` intentionally raises `ImportError` due to a circular import. Do not treat this as an accidental bug.

## Code quality checks

Run from the repository root after installing `flake8` and `mypy` in your chosen development environment:

```bash
flake8 . --exclude=.venv,venv,lab_env,__pycache__
mypy --strict --explicit-package-bases .
```

Some exercise scripts deliberately demonstrate invalid operations. In particular, `ft_alembic_1.py` accesses an attribute that is not exposed by the package, and `ft_kaboom_1.py` triggers a circular-import failure. Keep these intentional failures in mind when reviewing results.

## Topics to understand for the 42 evaluation

- What a virtual environment isolates (and what it does not)
- `sys.prefix`, `sys.base_prefix`, and `sys.executable`
- `pip`, `requirements.txt`, `pyproject.toml`, and `poetry.lock`
- `.env`, `load_dotenv()`, `os.getenv()`, and `os.environ`
- Environment-variable precedence and protecting secrets
- Modules vs packages; the role of `__init__.py` and `__all__`
- `import ...` vs `from ... import ...`
- Absolute vs relative imports
- Circular imports and partially initialized modules

## Notes

Run the scripts for Exercises 2–4 **from the repository root** so that the top-level `elements.py` module is importable. Python 3.10+ is required, and the project must follow the exercise-specific import restrictions.
