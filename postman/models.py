from django.db import models

# Create your models here.

class Change(models.Model):

    gender=models.CharField(max_length=128)
    photo=models.ImageField(upload_to='pic')
    location=models.CharField(max_length=128)
    description=models.CharField(max_length=128)
    nickname=models.CharField(max_length=128)
    province=models.CharField(max_length=128)
    city=models.CharField(max_length=128)
    password=models.CharField(max_length=128)

    class Meta():
        db_table='change_user'
