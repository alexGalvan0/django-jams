# Generated by Django 4.1.3 on 2022-11-16 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0002_rename_likes_song_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year_released',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(4)]),
        ),
    ]