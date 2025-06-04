from django.db import models

class Team(models.Model):
    SHOW_TYPES = [
        ('Cabaret', 'Cabaret'),
        ('Drag', 'Drag'),
        ('Burlesque', 'Burlesque'),
        ('Queer', 'Queer'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateField()
    city = models.CharField(max_length=100, default='')  # for filtering
    show_type = models.CharField(max_length=50, choices=SHOW_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='teams_images/')

