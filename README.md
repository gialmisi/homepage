# Personal webpage built with Material for MkDocs
This repository contains the contents and tools to build my own
personal website. A lot of the contents is generated using templates and
data stored in YAML files. This makes updating the contents easy. Modifying
the structure of the site is also straightforward since most can be achieved by simply
modifying the contents of markdown files.

## Dependencies
The project is build using Python, [MkDocs](https://www.mkdocs.org/),
and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). The
dependencies are listed in the file `pyproject.toml`.
Python version 3.12 and up is required.

## Building the project
The easiest way is utilizing Poetry. You can get Poetry [here](https://python-poetry.org/).

Using Poetry, first, initialize a virtual environment and activate it
with the command

```
poetry shell
```

Then, install the project

```
poetry install
```

Now you can build and serve the website with the command

```
mkdocs serve
```

This will run a local server that will serve the website by default
on `http://127.0.0.1:8000/`.

## Deploying on GitHub pages
To deploy the site on GitHub pages, follow the instructions in the
[mkdocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/#github-pages).

## Project structure
The website and its structure is configured in the file `mkdocs.yml`.

Most of the structure and rules to render the project are found in the directory `website`.

The directory `data` contains the contents of the website, specified in YAML files, and also
other data that is meant to be publicly shared.

## License
The project is under the MIT license.