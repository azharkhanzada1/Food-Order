from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects  = UserManager()