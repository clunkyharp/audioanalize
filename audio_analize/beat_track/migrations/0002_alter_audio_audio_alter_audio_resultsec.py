# Generated by Django 4.0.4 on 2022-05-23 15:00

import beat_track.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(upload_to='Users/amir/Desktop/audioanalize/audiofiles', validators=[beat_track.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='audio',
            name='resultsec',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
