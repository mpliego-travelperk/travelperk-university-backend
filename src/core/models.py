from django.db import models


class Recipe(models.Model):
    """Recipe model object"""
    name = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255,
        blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient model object"""
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE)
    unique_together = ['name', 'recipe']

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'recipe']
