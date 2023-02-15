#!/bin/sh
npm install
poetry env use $(pyenv which python)
poetry install
