# Generated by Django 3.0.4 on 2020-03-24 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200324_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
    ]
