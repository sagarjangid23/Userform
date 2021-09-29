from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserDetail(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=False)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField()