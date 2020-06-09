from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.FileField(max_length=20)
    upload_time=models.DateTimeField(auto_now=True)
    pulish_time=models.DateField(auto_now_add=True)
    status=models.BooleanField()
    content=models.TextField(null=True)
    img=models.ImageField(upload_to='pic')

    class Meta():
        db_table='t_Article'


class Img(models.Model):
    img = models.ImageField(upload_to='pic')

    class Meta():
        db_table='t_img'