from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []