# python-project-initializer

MacOS shell script to initialize a new, structured Python project.

### Prerequisites
+ Python3

### Dependencies

Install them by following the provided links:
+ [poetry](https://python-poetry.org/docs/master/#installation)
    + if you (like me) like to have the virtualenv in a `.venv` folder within the project, you can [configure poetry](https://python-poetry.org/docs/configuration/#virtualenvsin-project) accordingly by running: `poetry config virtualenvs.in-project true` 
    + the current poetry configuration can be found running: `poetry config --list`
+ [helm](https://formulae.brew.sh/formula/helm)
+ [git-flow](https://formulae.brew.sh/formula/git-flow)
+ [tree](https://formulae.brew.sh/formula/tree)