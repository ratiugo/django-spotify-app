# Generated by Django 3.0.3 on 2020-03-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioFromRecentlyPlayedTracks', '0009_track_valence'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='image_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]