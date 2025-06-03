from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='teams_images/')

