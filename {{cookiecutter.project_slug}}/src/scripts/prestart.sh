#! /usr/bin/env sh

# Apply migrations https://docs.djangoproject.com/en/3.2/ref/django-admin/#migrate
poetry run python manage.py migrate

# Collect static https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#collectstatic
poetry run python manage.py collectstatic --noinput

# Compile i18n messages https://docs.djangoproject.com/en/3.2/ref/django-admin/#compilemessages
poetry run python manage.py compilemessages --use-fuzzy
