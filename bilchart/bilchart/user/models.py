from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
