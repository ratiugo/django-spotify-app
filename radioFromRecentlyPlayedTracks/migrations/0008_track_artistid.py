# Generated by Django 3.0.3 on 2020-03-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioFromRecentlyPlayedTracks', '0007_track_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artistID',
            field=models.CharField(max_length=100, null=True),
        ),
    ]