### {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}


## INSTALLATION
### Local development

This tutorial describes the installation using [pyenv][pyenv], [pyenv-virtualenv][pyenv-virtualenv] and installing [poetry][poetry] in the local environment of the project. However, you can use any alternative way convenient for you: use [virtualenv][virtualenv], install [poetry][poetry] globally, or stop using [pyenv][pyenv] in favor of a global [python][python] interpreter. But it will not be described, do it at one's own risk.

 1. Install [pyenv][pyenv]: [instruction](https://github.com/pyenv/pyenv#installation)

 2. Install [python][python] 3.9.x with [pyenv][pyenv]. For example:
    ```shell
    pyenv install 3.9.6
    ```
    *_Here and in other the examples, [python][python] version [3.9.6](https://www.python.org/downloads/release/python-396/) will be used. You can use any minor version 3.9.x._

 3. Install [pyenv-virtualenv][pyenv-virtualenv]: [Instruction](https://github.com/pyenv/pyenv-virtualenv#installation)

 4. Create [virtualenv][pyenv-virtualenv]:
    ```shell
    pyenv virtualenv 3.9.6 {{ cookiecutter.project_slug }}
    ```
    *_`{{ cookiecutter.project_slug }}` - [virtualenv][pyenv-virtualenv] name. You can change it with your custom name._

 5. Set the local application-specific [virtualenv][pyenv-virtualenv]:
     ```shell
     pyenv local {{ cookiecutter.project_slug }}
     ```

 6. Install [poetry][poetry]: [Instruction](https://python-poetry.org/docs/#installation)

 7. Install project dependencies:
    ```shell
    poetry install
    ```
 8. Install [PostgreSQL][postgres] if not installed: [Instruction](https://www.postgresql.org/download/)

 9. [Create a database](https://www.postgresql.org/docs/12/sql-createdatabase.html) in any convenient way

 10. Copy [`.env.sample`](.env.sample) with file named `.env`:
     ```shell
     cp .env.sample .env
     ```
 11. Set values for variables (values should replace `<...>`).

 12. Go to the folder with the source code of the project:
     ```shell
     cd src
     ```

 13. Apply [migrations](https://docs.djangoproject.com/en/3.2/topics/migrations/):
     ```shell
     ./manage.py migrate
     ```

 14. Run [development server](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#the-development-server):
    ```shell
    ./manage.py runserver
    ```

 15. You are gorgeous! The app is running and most likely available at http://127.0.0.1:8000/

### Deployment:
This manual describes the delivery of an application using [docker][docker]. You can deliver the application using [docker-compose][docker-compose], even abandon [docker][docker] and put everything on the server or use other methods and tools, but this will not be described, and you will have to do this at one's own risk.

 1. Install and configure [docker][docker]: [instruction](https://docs.docker.com/engine/install/ubuntu/)

 2. Build [image](https://docs.docker.com/glossary/#image) from [dockerfile](https://docs.docker.com/glossary/#dockerfile):
    ```shell
    docker build . --build-arg SSH_PRIVATE_KEY=<SSH_PRIVATE_KEY> --tag {{ cookiecutter.project_slug }}
    ```
    _`SSH_PRIVATE_KEY` - [ssh][ssh] private [key](https://www.ssh.com/academy/ssh/key), which is used to access the [git][git] [repositories](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) where the source code of the custom private libraries is stored_
    
    _`{{ cookiecutter.project_slug }}` - name of the [image](https://docs.docker.com/glossary/#image) [tag](https://docs.docker.com/engine/reference/commandline/build/#tag-an-image--t). Can be replaced with a custom value_

 3. Run [container](https://docs.docker.com/glossary/#container):
    ```shell
    docker run \
      --env SECRET_KEY=<DJANGO_SECRET_KEY> \
      --env DATABASE_URL=<DATABASE_URL> \
      --env SENTRY_DSN=<SENTRY_DSN> \
      --env DJANGO_STATIC_ROOT=<DJANGO_STATIC_ROOT> \
      --env ALLOWED_HOSTS=<ALLOWED_HOSTS> \
      --name {{ cookiecutter.project_slug }}-backend \
      {{ cookiecutter.project_slug }}
    ```
    where instead of `<...>` specify the corresponding values. For more information on environment variables, see the section on [environment variables](#environment-variables).

    _`{{ cookiecutter.project_slug }}-backend` - [container](https://docs.docker.com/glossary/#container) [name](https://docs.docker.com/engine/reference/run/#name---name). Can be replaced with custom value_

    _`{{ cookiecutter.project_slug }}` - name of the [image](https://docs.docker.com/glossary/#image) [tag](https://docs.docker.com/engine/reference/commandline/build/#tag-an-image--t). Specified in step 2_
    

## Environment variables
Name | Required | Default value | Description
--- | --- | --- | ---
DEBUG              | :heavy_minus_sign: | `False`           | A boolean that turns on/off [debug mode][1] in django |
SECRET_KEY         | :heavy_plus_sign:  | N/A               | [Secret key][2] for django-project |
DATABASE_URL       | :heavy_plus_sign:  | N/A               | Link to connect to the database. Link to connect to the database. [This format][4] is used |
DJANGO_STATIC_ROOT | :heavy_minus_sign: | <BASE_DIR>/static | Directory for storing [static files][4] |
SENTRY_DSN         | :heavy_minus_sign: | `None`            | [Sentry DSN][5] |
ALLOWED_HOSTS      | :heavy_plus_sign:  | `[]`              | Django [ALLOWED_HOSTS](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts)
[1]: https://docs.djangoproject.com/en/3.2/ref/settings/#debug
[2]: https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
[4]: https://django-environ.readthedocs.io/en/latest/#environ.environ.Env.db_url
[4]: https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
[5]: https://docs.sentry.io/product/sentry-basics/dsn-explainer/


[pyenv]: https://github.com/pyenv/pyenv
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[python]: https://python.org
[poetry]: https://python-poetry.org
[postgres]: https://www.postgresql.org
[virtualenv]: https://packaging.python.org/key_projects/#virtualenv
[docker]: https://www.docker.com
[docker-compose]: https://docs.docker.com/compose/
[ssh]: https://www.openssh.com
[git]: https://git-scm.com
