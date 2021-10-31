# python-project-initializer

MacOS shell script to initialize a new, structured Python project.

### Prerequisites
+ Python3
+ Git
    + GitHub changed the default branch name from `master` to `main`, thus to suppress a potential warning from `git init` update your `git` config by running: `git config --global init.defaultBranch main`

### Dependencies

Install them by following the provided links:
+ [poetry](https://python-poetry.org/docs/master/#installation)
    + if you (like me) like to have the virtualenv in a `.venv` folder within the project, you can [configure poetry](https://python-poetry.org/docs/configuration/#virtualenvsin-project) accordingly by running: `poetry config virtualenvs.in-project true` 
    + the current poetry configuration can be found running: `poetry config --list`
+ [helm](https://formulae.brew.sh/formula/helm)  
+ [tree](https://formulae.brew.sh/formula/tree)

Bonus point (not needed):
+ [git-flow](https://formulae.brew.sh/formula/git-flow)
#### TL;DR

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
brew install helm tree
# brew install git-flow  # if you want
```

### Run
```shell
ppi <project-name> "<project-description>"
```

Example log:
```shell
$ ppi super-frontend "A super frontend"

[Init] > Project structure
Created package super_frontend in super-frontend

[Init] > README

[Init] > .gitignore

[Init] > License

[Init] > Docker

[Init] > Jenkins

[Init] > Scripts

[Init] > Setuptools

[Init] > Helm
Creating scripts/deployments/super-frontend

[Init] > Git
Initialized empty Git repository in /Users/abc/custom/path/super-frontend/.git/
No branches exist yet. Base branches must be created now.
Branch name for production releases: [master] main
Branch name for "next release" development: [develop] 

How to name your supporting branch prefixes?
Feature branches? [feature/] 
Release branches? [release/] 
Hotfix branches? [hotfix/] 
Support branches? [support/] 
Version tag prefix? [] 

[Init] > Done

.
├── LICENSE
├── README.md
├── docker
│   └── Dockerfile
├── jenkins
│   └── Jenkinsfile
├── pyproject.toml
├── scripts
│   ├── _conf.sh
│   ├── deployments
│   │   └── super-frontend
│   │       ├── Chart.yaml
│   │       ├── charts
│   │       ├── templates
│   │       │   ├── NOTES.txt
│   │       │   ├── _helpers.tpl
│   │       │   ├── deployment.yaml
│   │       │   ├── hpa.yaml
│   │       │   ├── ingress.yaml
│   │       │   ├── service.yaml
│   │       │   ├── serviceaccount.yaml
│   │       │   └── tests
│   │       │       └── test-connection.yaml
│   │       └── values.yaml
│   ├── docker-build.sh
│   ├── docker-clean.sh
│   ├── docker-push.sh
│   └── docker-run.sh
├── setup.py
├── super_frontend
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_super_frontend.py

10 directories, 24 files
```