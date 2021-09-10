#!/bin/bash -e



echo Generating .env file...

echo SECRET_KEY="{{ cookiecutter.ENV_SECRET_KEY }}" > .env
echo DEBUG="{{ cookiecutter.ENV_DEBUG }}" >> .env
echo DATABASE_URL="{{ cookiecutter.ENV_DATABASE_URL }}" >> .env
echo DJANGO_STATIC_ROOT="{{ cookiecutter.ENV_DJANGO_STATIC_ROOT }}" >> .env
echo ALLOWED_HOSTS="{{ cookiecutter.ENV_DJANGO_ALLOWED_HOSTS }}" >> .env

{% if cookiecutter.use_sentry == "yes" %}echo  SENTRY_DSN="{{ cookiecutter.ENV_SENTRY_DSN }}" >> .env {% endif %}

echo Done
