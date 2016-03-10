from django.db import models
from django.conf import settings


class BaseShadowAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    email = models.EmailField(
        blank=True,
        null=True,
        unique=True
    )

    class Meta:
        abstract = True


class ShadowAccount(BaseShadowAccount):
    class Meta:
        swappable = 'BABIK_ACCOUNT_MODEL'
