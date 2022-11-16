# Generated by Django 4.1.3 on 2022-11-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0006_alter_song_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(blank=True, to='jams.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]