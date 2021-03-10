import os
import datetime
from django.db import models
from uuid import uuid4
from django.conf import settings
from django.core import signing
from django.contrib.auth.models import AbstractUser

# Create your models here.

def profile_picture(obj, filename):

    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)

    path = 'users/{}/profile/'.format(obj.email)

    return os.path.join(path, filename)

class User(AbstractUser):

    USER_ROLE = (
        (1, ("Admin")),
        (2, ("Teacher")),
        (3, ("Student")),
    )

    type = models.IntegerField(choices=USER_ROLE, verbose_name='Rol', default=3)
    photo = models.ImageField(upload_to=profile_picture, blank=True, null=True, verbose_name='profile_picture')
    full_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
