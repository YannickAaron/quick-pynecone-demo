# Python default project

## Prerequisites

### Install Homebrew
install homebrew

### Install pyenv

### install prepare: ./husky/prepare

# PythonDefaultProject
Python Default to use for new Projects

pytest: just name file _test.py


poetry run python poetry-update.py -> build an npm package



## Pre Commit

**[General](https://github.com/pre-commit/pre-commit-hooks)**
Repo: [https://github.com/pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

Some out-of-the-box hooks for pre-commit.




## TODO
- [ ] add a script that automatically creates the structure needed for the project
    - The script should be able to init poetry with the standard packages needed for the pre-commit hook
    - The script should install husky if needed
    - The script should differentiate between different needs for the project (e.g. notebook, code)
    - The script should be able to select the pre-commit hook
- [ ] add dependbot
