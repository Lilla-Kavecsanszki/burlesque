from django.db import models

class Show(models.Model):
    SHOW_TYPES = [
        ('Cabaret', 'Cabaret'),
        ('Drag', 'Drag'),
        ('Burlesque', 'Burlesque'),
        ('Queer', 'Queer'),
    ]

    title = models.CharField(max_length=100)
    featured_on_homepage = models.BooleanField(default=False) # for paid display
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default='')  # for filtering
    date = models.DateField()
    show_type = models.CharField(max_length=50, choices=SHOW_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    booking_link = models.URLField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='shows_images/')
    created_at = models.DateTimeField(auto_now_add=True)