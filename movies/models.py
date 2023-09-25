from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100,  verbose_name="Movie Title")
    description = models.TextField(verbose_name="Presentation")
    image = models.CharField(max_length=50)
    year = models.IntegerField(verbose_name="Release Year")
    duration = models.IntegerField(verbose_name="Duration (mins)")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    isReleased = models.BooleanField(default=True, verbose_name="Released")

    def __str__(self):
        return f"{self.name} ({self.year})"