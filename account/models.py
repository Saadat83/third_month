from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.user} {self.phone_number}'


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

