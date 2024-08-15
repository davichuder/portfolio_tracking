from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False)
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    registration_method = models.CharField(
        max_length=15,
        choices=REGISTRATION_CHOICES,
        default='email'
    )

    def __str__(self):
        return self.username
