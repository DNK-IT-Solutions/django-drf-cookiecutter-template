"""
WSGI config for {{cookiecutter.django_settings_package}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.django_settings_package}}.settings")

application = get_wsgi_application()
