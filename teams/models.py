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
    main_image = models.ImageField(upload_to='teams_images/')

    def __str__(self):
        return self.name


class TeamImage(models.Model):
    team = models.ForeignKey(
        Team, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="teams_gallery/")

    def __str__(self):
        return f"Image for {self.team.name}"


class TeamVideo(models.Model):
    team = models.ForeignKey(
        Team, related_name="videos", on_delete=models.CASCADE
    )
    video = models.FileField(
        upload_to="videos/",
        blank=True,
    )

    def __str__(self):
        return f"Video for {self.team.name}"
