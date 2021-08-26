from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from auditlog.registry import auditlog


class User(AbstractUser):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"
        indexes = (models.Index(fields=("email",)), models.Index(fields=("username",)))


auditlog.register(User)
