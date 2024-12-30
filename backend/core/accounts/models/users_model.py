from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from accounts.managers import CustomUserManager



class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("Email Address",max_length=254,unique=True)
    is_admin = models.BooleanField(default=False)
    is_validator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    created_date = models.DateField(auto_now=False, auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'

        permissions=[
            ('validate_data',"can validate data and report it"),
            ('content_management',"can manage content of site(only owner's data)")
        ]

    def __str__(self):
        return self.email
    
