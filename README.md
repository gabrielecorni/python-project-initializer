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
    + GitHub changed the default branch name from `master` to `main`, thus to suppress a potential warning from `git init` update your `git` config by running: `git config --global init.defaultBranch main`
+ [tree](https://formulae.brew.sh/formula/tree)

#### TL;DR

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
brew install helm git-flow tree
```

### Run
```shell
ppi <project-name> "<project-description>"
```