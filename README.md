# django-drf-cookiecutter-template
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/DNK-IT-Solutions/django-drf-cookiecutter-template/main)](https://github.com/DNK-IT-Solutions/django-drf-cookiecutter-template/commits/main)
![last build](https://github.com/DNK-IT-Solutions/django-drf-cookiecutter-template/actions/workflows/test_create_project.yml/badge.svg)


[Django][django] + [DRF][drf] + [Poetry](https://python-poetry.org) template for [cookiecutter][cookiecutter]


## Dependencies:
 * [Python 3.9](https://www.python.org/downloads/release/python-390/)
 * [python-pip](https://pypi.org/project/pip/)
 * [PostgreSQL][postgres]


 
## Installation

 1. If necessary, create and activate a [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment) in one of the following ways:
    - [with pyenv](https://github.com/pyenv/pyenv-virtualenv#usage)
    - [with virtualenv](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

    Or in another way compatible with poetry
 2. Install [cookiecutter][cookiecutter] using [this instruction](https://cookiecutter.readthedocs.io/en/latest/installation.html)
 3. Run [postgres][postgres] server and create database for project
 4. Create project from template:
    ```shell
    cookiecutter gh:DNK-IT-Solutions/django-drf-cookiecutter-template
    ```
    For interactive project creation

    OR
    ```shell
    cookiecutter gh:DNK-IT-Solutions/django-drf-cookiecutter-template \
        --no-input \
        project_name=<project_name> \
        project_slug=<project_slug> \
        project_description=<project_description> \
        project_version=<project_version> \
        django_settings_package=<django_settings_package> \
        author=<author> \
        use_sentry=<use_sentry> \
        ENV_DEBUG=<ENV_DEBUG> \
        ENV_SECRET_KEY=<ENV_SECRET_KEY> \
        ENV_DATABASE_URL=<ENV_DATABASE_URL> \
        ENV_DJANGO_STATIC_ROOT=<ENV_DJANGO_STATIC_ROOT> \
        ENV_SENTRY_DSN=<ENV_SENTRY_DSN> \
        ENV_DJANGO_ALLOWED_HOSTS=<ENV_DJANGO_ALLOWED_HOSTS>
    ```
    To run without asking for user input
 
    In one case or another - you need to set values for some parameters, the descriptions of which you can read [here](#Template-parameters)

![clean display](https://user-images.githubusercontent.com/17884471/131993262-20807241-df82-4724-8e5b-e5cf481181d4.gif)


## Template parameters ##

| Parameter name           | Required              | Description |
| ------------------------ |:---------------------:|:----------- |
| project_name             | :heavy_plus_sign:     | The name of the project. Will be used in the [README.md](./{{cookiecutter.project_slug}}/README.md) file. It also creates a default value for the `project_slug` variable from this value. |
| project_slug             | :heavy_minus_sign:    | Used for the name of the root directory of the Django project, `[tool.poetry].name` value in [pyproject.toml][2], also as the default database name in the `ENV_DATABASE_URL` variable |
| project_description      | :heavy_minus_sign:    | Used in [README.md](./{{cookiecutter.project_slug}}/README.md), `[tool.poetry].description` value in [pyproject.toml][2] |
| project_version          | :heavy_minus_sign:    | Used as `[tool.poetry].version` value in [pyproject.toml][2] |
| django_settings_package  | :heavy_minus_sign:    | The name of the configuration django application (the application that stores the settings.py file) |
| author_name              | :heavy_plus_sign:     | Used as part of `[tool.poetry].authors` value in [pyproject.toml][2] |
| author_email             | :heavy_plus_sign:     | Used as part of `[tool.poetry].authors` value in [pyproject.toml][2], [drf-yasg][drf-yasg] contact email |
| use_sentry               | :heavy_minus_sign:    | Determines whether [sentry][3] will be used in the project. If yes, [sentry-sdk][4] will be installed and configured |
| ENV_DEBUG                | :heavy_minus_sign:    | Used to generate .env file. A boolean that turns on/off [debug mode][5] in django |
| ENV_SECRET_KEY           | :heavy_minus_sign:    | Used to generate .env file. [Secret key][6] for django-project |
| ENV_DATABASE_URL         | :heavy_minus_sign:    | Used to generate .env file. Link to connect to the database. Link to connect to the database. [This format][7] is used |
| ENV_DJANGO_STATIC_ROOT   | :heavy_minus_sign:    | Used to generate .env file. Directory for storing [static files][8] |
| ENV_SENTRY_DSN           | if use_sentry = "yes" | Used to generate .env file. [Sentry DSN][9] only if use_sentry = "yes" |
| ENV_DJANGO_ALLOWED_HOSTS | :heavy_minus_sign:    | Used to generate .env file. Django [ALLOWED_HOSTS](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts)

[1]: https://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html#random-string-extension
[2]: ./{{cookiecutter.project_slug}}/pyproject.toml
[3]: https://sentry.io/
[4]: https://github.com/getsentry/sentry-python
[5]: https://docs.djangoproject.com/en/3.2/ref/settings/#debug
[6]: https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
[7]: https://django-environ.readthedocs.io/en/latest/#environ.environ.Env.db_url
[8]: https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
[9]: https://docs.sentry.io/product/sentry-basics/dsn-explainer/

 You can see the default value in the [configuration file](./cookiecutter.json)

## What's included in the template?
This template is intended for creating API applications, therefore it does not include libraries that extend the functionality of templates

 * [Django][django]
 * [DRF]
 * [drf-yasg][drf-yasg] - for API documentation
 * [django-auditlog](https://github.com/jazzband/django-auditlog)
 * [django-environ-2](https://django-environ-2.readthedocs.io/en/stable/)
#### Development tools:
 * [flake8](https://flake8.pycqa.org/en/latest/) with plugins:
    - [flake8-absolute-import](https://github.com/bskinn/flake8-absolute-import)
    - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
    - [flake8-cognitive-complexity](https://github.com/Melevir/flake8-cognitive-complexity)
    - [flake8-commas](https://github.com/PyCQA/flake8-commas)
    - [flake8-django](https://github.com/rocioar/flake8-django)
    - [flake8-eradicate](https://github.com/wemake-services/flake8-eradicate)
    - [flake8-isort](https://github.com/gforcada/flake8-isort)
    - [flake8-fixme](https://github.com/tommilligan/flake8-fixme)
    - [flake8-mock](https://github.com/aleGpereira/flake8-mock)
    - [flake8-multiline-containers](https://github.com/jsfehler/flake8-multiline-containers)
    - [flake8-mutable](https://github.com/ebeweber/flake8-mutable)
    - [flake8-pep3101](https://github.com/gforcada/flake8-pep3101)
    - [flake8-pie](https://github.com/sbdchd/flake8-pie)
    - [flake8-print](https://github.com/JBKahn/flake8-print)
    - [flake8-printf-formatting](https://github.com/atugushev/flake8-printf-formatting)
    - [flake8-pytest](https://github.com/tholo/pytest-flake8)
    - [flake8-pytest-style](https://github.com/m-burst/flake8-pytest-style)
    - [flake8-quotes](https://github.com/zheller/flake8-quotes)
    - [flake8-simplify](https://github.com/MartinThoma/flake8-simplify)
    - [flake8-todo](https://github.com/schlamar/flake8-todo)
    - [flake8-use-fstring](https://github.com/MichaelKim0407/flake8-use-fstring)
    - [flake8-variables-names](https://github.com/best-doctor/flake8-variables-names)
    - [flake8-walrus](https://github.com/asottile/flake8-walrus)
 * [mypy](https://mypy.readthedocs.io/en/stable/)
 * [bandit](https://github.com/PyCQA/bandit)
 * [black](https://black.readthedocs.io/en/stable/)
 * [isort](https://github.com/PyCQA/isort)
 * [django-nose](https://github.com/jazzband/django-nose)
 * [coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
 * [factory-boy](https://factoryboy.readthedocs.io/en/stable/)


More information can be found in the [pyproject.toml](./\{\{cookiecutter.project_slug\}\}/pyproject.toml) file


[drf-yasg]: https://drf-yasg.readthedocs.io/en/stable/
[django]: https://www.djangoproject.com
[drf]: https://www.django-rest-framework.org
[cookiecutter]: https://cookiecutter.readthedocs.io/
[postgres]: https://www.postgresql.org
