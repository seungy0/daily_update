from django.db import models

# Create your models here.


class Bilchart(models.Model):
    rank = models.IntegerField(primary_key=True)
    song = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bilchart'


class vege(models.Model):
    name = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    price = models.IntegerField()
