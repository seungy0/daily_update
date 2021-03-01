from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.


# class User(models.Model):
#     user_id = models.CharField(max_length=20)
#     user_name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)

#     class Meta:
#         db_table = 'users'


# class myUser(AbstractBaseUser):
#     user_id = models.CharField(max_length=20, unique=True)
#     user_name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     USERNAME_FIELD = 'user_id'
#     REQUIRED_FIELDS = ['user_name', 'email', 'password', 'phone']


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_id, user_name, email, phone, password=None):
        if not user_id:
            raise ValueError('must have user id')
        elif not user_name:
            raise ValueError('must have user name')
        elif not email:
            raise ValueError('must have user email')
        elif not phone:
            raise ValueError('must have user phone')
        user = self.model(
            user_id=user_id,
            user_name=user_name,
            email=self.normalize_email(email),
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_name, email, phone, password):
        user = self.create_user(
            user_id=user_id,
            user_name=user_name,
            email=self.normalize_email(email),
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    user_id = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    user_name = models.CharField(
        max_length=20,
        null=False,
        unique=False
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    phone = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['user_name', 'email', 'user_id', 'phone']
