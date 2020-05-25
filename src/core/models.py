from django.db import models


class Recipe(models.Model):
    """Recipe model object"""
    name = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255,
        blank=True)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient model object"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
