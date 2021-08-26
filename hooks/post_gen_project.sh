#!/bin/bash -e

echo -ne "Running with "

python --version

echo Creating and populating virtualenv..

make install-deps

cd src

echo Collecting static assets...
./manage.py collectstatic

echo Running initial migrations...
./manage.py migrate

cd ../
echo Running linters, vulnerability checking, type checking
make analyze-source-code

echo Running test...
make test

echo Git initializing
git init
git add --all && git commit -m"Init django-project"

echo Done
