from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

