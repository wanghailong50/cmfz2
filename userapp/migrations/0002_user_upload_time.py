# Generated by Django 2.0.6 on 2020-06-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='upload_time',
            field=models.DateField(auto_now=True),
        ),
    ]