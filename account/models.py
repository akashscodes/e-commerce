from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import ActiveUserManager, CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    active_users = ActiveUserManager()

    class Meta:
        db_table = 'User_Account'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True)
    address_line_1 = models.CharField(max_length=70)
    address_line_2 = models.CharField(max_length=70, null=True, blank=True)
    city = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=20)
    landmark = models.CharField(max_length=30)

    class Meta:
        db_table = 'User_Profile'

    @property
    def full_name(self):
        "Returns person's full name"
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name
