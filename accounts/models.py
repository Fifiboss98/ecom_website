from django.db import models
from django.contrib.auth.models import AbstractUser


class Shoper(AbstractUser):

    def __str__(self):
        return self.username
