import os
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

UserModel = get_user_model()

class BaseModels(models.Model):

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_owner"
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True
    )

    class Meta:
        abstract = True 