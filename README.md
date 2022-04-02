# Example application code for the python architecture book

## Chapters

Each chapter has its own branch which contains all the commits for that chapter,
so it has the state that corresponds to the _end_ of that chapter.
If you want to try and code along with a chapter,
you'll want to check out the branch for the previous chapter.

https://github.com/cosmicpython/code/branches/all


## Exercises

Branches for the exercises follow the convention `{chapter_name}_exercise`,
eg https://github.com/cosmicpython/code/tree/chapter_04_service_layer_exercise


## Requirements

* docker with docker-compose
* for chapters 1 and 2, and optionally for the rest: a local python3.8 virtualenv


## Building the containers

_(this is only required from chapter 3 onwards)_

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```

## Creating a local virtualenv (optional)

```sh
poetry install
```

To activate the virtualenv:

```sh
poetry shell
```


## Running the tests

```sh
make test
# or, to run individual test types
make unit-tests
make integration-tests
make e2e-tests
# or, if you have a local virtualenv
make up
poetry run pytest tests/unit
poetry run pytest tests/integration
poetry run pytest tests/e2e
```

## Makefile

There are more useful commands in the makefile, have a look and try them out.

