# django-drf-cookiecutter-template
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/DNK-IT-Solutions/django-drf-cookiecutter-template/main)](https://github.com/DNK-IT-Solutions/django-drf-cookiecutter-template/commits/main)


[Django](https://www.djangoproject.com) + [DRF](https://www.django-rest-framework.org) + [Poetry](https://python-poetry.org) template for [cookiecutter](https://cookiecutter.readthedocs.io/)

## Dependencies:
 * [Python 3.9](https://www.python.org/downloads/release/python-390/)
 * 

---
 
## Installation

 1. If necessary, create and activate a [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment) in one of the following ways:
    - [with pyenv](https://github.com/pyenv/pyenv-virtualenv#usage)
    - [with virtualenv](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

    Or in another way compatible with poetry
 2. Install [cookiecutter](https://cookiecutter.readthedocs.io/) using [this instruction](https://cookiecutter.readthedocs.io/en/latest/installation.html)
 3. Create project from template:
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
        ENV_SENTRY_DSN=<ENV_SENTRY_DSN>
    ```
    To run without asking for user input
 
    In one case or another - you need to set values for some parameters, the descriptions of which you can read [here](#Template-parameters)
---

## Template parameters ##

| Parameter name          | Required              | Description |
| ----------------------- |:---------------------:|:----------- |
| project_name            | :heavy_plus_sign:     | The name of the project. Will be used in the [README.md](./{{cookiecutter.project_slug}}/README.md) file. It also creates a default value for the `project_slug` variable from this value. |
| project_slug            | :heavy_minus_sign:    | Used for the name of the root directory of the Django project, `[tool.poetry].name` value in [pyproject.toml][2], also as the default database name in the `ENV_DATABASE_URL` variable |
| project_description     | :heavy_minus_sign:    | Used in [README.md](./{{cookiecutter.project_slug}}/README.md), `[tool.poetry].description` value in [pyproject.toml][2] |
| project_version         | :heavy_minus_sign:    | Used as `[tool.poetry].version` value in [pyproject.toml][2] |
| django_settings_package | :heavy_minus_sign:    | The name of the configuration django application (the application that stores the settings.py file) |
| author_name             | :heavy_plus_sign:     | Used as part of `[tool.poetry].authors` value in [pyproject.toml][2] |
| author_email            | :heavy_plus_sign:     | Used as part of `[tool.poetry].authors` value in [pyproject.toml][2], [drf-yasg][10] contact email |
| use_sentry              | :heavy_minus_sign:    | Determines whether [sentry][3] will be used in the project. If yes, [sentry-sdk][4] will be installed and configured |
| ENV_DEBUG               | :heavy_minus_sign:    | Used to generate .env file. A boolean that turns on/off [debug mode][5] in django |
| ENV_SECRET_KEY          | :heavy_minus_sign:    | Used to generate .env file. [Secret key][6] for django-project |
| ENV_DATABASE_URL        | :heavy_minus_sign:    | Used to generate .env file. Link to connect to the database. Link to connect to the database. [This format][7] is used |
| ENV_DJANGO_STATIC_ROOT  | :heavy_minus_sign:    | Used to generate .env file. Directory for storing [static files][8] |
| ENV_SENTRY_DSN          | if use_sentry = "yes" | Used to generate .env file. [Sentry DSN][9] only if use_sentry = "yes" |

[1]: https://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html#random-string-extension
[2]: ./{{cookiecutter.project_slug}}/pyproject.toml
[3]: https://sentry.io/
[4]: https://github.com/getsentry/sentry-python
[5]: https://docs.djangoproject.com/en/3.2/ref/settings/#debug
[6]: https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
[7]: https://django-environ.readthedocs.io/en/latest/#environ.environ.Env.db_url
[8]: https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
[9]: https://docs.sentry.io/product/sentry-basics/dsn-explainer/
[10]: https://drf-yasg.readthedocs.io/en/stable/

 You can see the default value in the [configuration file](./cookiecutter.json)
