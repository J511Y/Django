# Generated by Django 3.1.2 on 2020-11-09 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily',
            name='like',
        ),
    ]
