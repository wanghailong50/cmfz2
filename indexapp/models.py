from django.db import models

# Create your models here.


class Slides(models.Model):
    titile=models.FileField(max_length=20)
    img=models.ImageField(upload_to='pic')
    upload_time=models.DateField(auto_now=True)
    is_show=models.BooleanField()