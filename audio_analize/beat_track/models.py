from distutils.command.upload import upload
from turtle import update
from venv import create
from django.conf.locale import sr
from django.db import models
from django.forms import ImageField
import librosa
from django.dispatch import receiver
from django.db.models.signals import post_save
from librosa.beat import beat_track
from matplotlib import image
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import librosa as _librosa
import librosa.display
matplotlib.use("macOSX")


class Audio(models.Model):
    title = models.CharField(max_length=30, null=True)
    artist = models.CharField(max_length=60, null=True)
    audio = models.FileField(upload_to='Users/amir/Documents/audioanalize/audio_analize/media')
    result = models.FloatField(max_length=60, blank=True)
    resultsec = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='Users/amir/Documents/audioanalize/audio_analize/media', blank=True)
    
    def __str__(self):
        return "%s" % self.artist
          

def beat_track_post_save(sender, instance, created, **kwargs):
    if created:
        y, sr = librosa.load(instance.audio)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        #plt.figure(figsize=(14, 5))
        #librosa.display.waveplot(y, sr=sr)

        filename = str(instance.audio).split('/')
        artist = filename[5].split('-')[0].replace('_', ' ')
        title = filename[5].split('-')[1].replace('_', ' ')

        #instance.image = librosa.display.waveplot(y, sr=sr)
        img = librosa.display.waveshow(y, sr=sr)
        instance.resultsec = int(tempo)
        instance.artist = artist
        instance.title = title

        instance.save()
    

post_save.connect(beat_track_post_save, sender=Audio)
