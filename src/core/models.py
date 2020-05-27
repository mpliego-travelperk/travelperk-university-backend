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
        related_name="ingredients",
        on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Overrides save prohibiting saving the same ingredient per recipe"""
        if self.id is None:
            results = Ingredient.objects.filter(
                name=self.name, recipe=self.recipe)
            if len(results) > 0:
                self.id = results[0].id
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
