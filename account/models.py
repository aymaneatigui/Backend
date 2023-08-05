from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class MyUserManager(BaseUserManager):
    def create_user(self, username ,email, first_name, last_name, password):
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username ,email, first_name, last_name, password):
        user = self.create_user(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user

class MyUser(AbstractUser):
    
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    refresh_token = models.TextField(blank=True, null=True) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = MyUserManager()

    def __str__(self) -> str:
        return f"{self.username} / {self.email}"
