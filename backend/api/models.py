from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES, default=OTHER)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, related_name='works')

    def __str__(self):
        return f'{self.artist} - {self.work_type} - {self.link}'
