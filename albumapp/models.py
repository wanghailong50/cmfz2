from django.db import models

# Create your models here.


class Album(models.Model):
    name=models.FileField(max_length=20)
    grade=models.FileField(max_length=20)
    author=models.FileField(max_length=20)
    play_people=models.FileField(max_length=20)
    number=models.FileField(max_length=20)
    content=models.TextField()
    pulish_time=models.DateField(auto_now=True)
    ready = models.CharField(max_length=100, blank=True, null=True)
    class Meta():
        db_table='t_Album'


class Chapter(models.Model):
    chapter_name=models.FileField(max_length=20)
    size=models.FileField(max_length=20)
    url=models.FileField(max_length=20)
    album_id = models.CharField(max_length=36, blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    chapter=models.ImageField(upload_to='pic',null=True)

    class Meta:
        db_table = 't_chapter'