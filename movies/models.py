from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=80, verbose_name="Full Name")
    birth_date = models.DateField(verbose_name="Birth Date")

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100,  verbose_name="Movie Title")
    description = models.TextField(verbose_name="Presentation")
    image = models.CharField(max_length=50)
    year = models.IntegerField(verbose_name="Release Year")
    duration = models.IntegerField(verbose_name="Duration (mins)")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    isReleased = models.BooleanField(default=True, verbose_name="Released")
    director = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} ({self.year})"