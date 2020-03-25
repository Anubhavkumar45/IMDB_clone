# Generated by Django 3.0.4 on 2020-03-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=10),
        ),
    ]
