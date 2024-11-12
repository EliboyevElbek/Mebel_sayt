from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    city = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=13)