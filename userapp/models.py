from django.db import models

# Create your models here.


class User(models.Model):
    phone=models.FileField(max_length=20)
    username=models.FileField(max_length=20)
    password=models.FileField(max_length=20)
    salt=models.TextField()
    address=models.FileField(max_length=20)
    sign=models.TextField()
    picture=models.ImageField(upload_to='pic')
    danger=models.BooleanField()
    wait=models.FileField(max_length=20)
    upload_time = models.DateField(auto_now=True)