# Generated by Django 3.0.4 on 2020-03-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20200325_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
