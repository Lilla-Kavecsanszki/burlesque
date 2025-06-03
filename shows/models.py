from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    dates = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='shows_images/')

