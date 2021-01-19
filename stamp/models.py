from django.db import models

# Create your models here.
class Stamp(models.Model):
    year = models.CharField(max_length=12)
    denomination = models.CharField(max_length=100)
    theme = models.ForeignKey('Theme', related_name='stamp_theme', on_delete=models.CASCADE)

    def __str__(self):
        return self.year


class Theme(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name