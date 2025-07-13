from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('monthly_3', '3€/mois'),
        ('annual_30', '30€/an'),
        ('monthly_7', '7€/mois'),
        ('annual_70', '70€/an'),
        ('monthly_20', '20€/mois'),
        ('annual_200', '200€/an'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.CharField(
        max_length=20, choices=SUBSCRIPTION_CHOICES, blank=True, null=True
    )
    subscribed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

