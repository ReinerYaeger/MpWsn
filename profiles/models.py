from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name
