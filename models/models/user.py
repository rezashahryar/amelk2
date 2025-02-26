from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_integer


class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=11, validators=[validate_integer], verbose_name='موبایل')
    is_agent = models.BooleanField(default=False, verbose_name='مشاور املاک هست')

    class Meta:
        permissions = [
            ('is_agent', 'has a real state company')
        ]
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.mobile:
            return self.mobile
        return self.email
