from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number, password=None):
        if not phone_number:
            raise ValueError("전화번호를 입력해주세요.")
        user = self.model(name=name, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, password=None):
        user = self.create_user(name=name, phone_number=phone_number, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    phone_number_validator = RegexValidator(
        regex=r'^\d+$',
        message='전화번호에는 숫자만 입력할 수 있습니다.'
    )
    phone_number = models.CharField(max_length=20, unique=True, validators=[phone_number_validator])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    point = models.IntegerField(default=999999)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name