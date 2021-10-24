#!/bin/bash

PROJECT_NAME=$1
PROJECT_DESC=$2

poetry new $PROJECT_NAME
cd $PROJECT_NAME

# README
mv README.rst README.md
echo "# $PROJECT_NAME" >> README.md
echo "$PROJECT_DESC" >> README.md

# .gitignore
curl -fsSL https://www.toptal.com/developers/gitignore/api/visualstudiocode,python,pycharm,jupyternotebooks,pycharm+all,pycharm+iml -o .gitignore

# LICENSE
curl -fsSL https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/main/LICENSE -o LICENSE

# Docker
mkdir docker
touch docker/Dockerfile

# Jenkins
mkdir jenkins
touch jenkins/Jenkinsfile

# scripts
mkdir scripts
# curl scripts from source

# setuptools

# helm

# git-flow

# Output
tree -R .