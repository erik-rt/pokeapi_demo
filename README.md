# PokeAPI Demo

The purpose of the project is to find the Pokemon generation with the greatest number of moves that start with the letter _"a"_ (case-insensitive). The answer is Generation IV which contains 9 moves that start with the letter _"a"_.

## Installation

The project uses [Poetry](https://python-poetry.org/docs/) for dependency management. After installation, `cd` into the project directory, run `poetry install` to install the dependencies, then run `poetry shell` to activate the virtual environment.

## Usage

The logic is included in a single file `poke_api/main.py`. To run the script yourself, run `python -m poke_api.main` from the root directory.

## Testing

There is a simple unit test included in the project. To run it, simply run `python -m unittest` from the root directory.
