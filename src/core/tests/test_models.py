from django.db import IntegrityError
from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_new_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient(name='Tomato')

        self.assertEqual(str(ingredient), ingredient.name)

    def test_new_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe(
            name='Tomato Sauce',
            description='Tomato Sauce Description')

        self.assertEqual(str(recipe), recipe.name)

    def test_same_name_different_recipe(self):
        """Test the ingredients of the same name are allow to be created"""
        recipe = models.Recipe.objects.create(name='Tomato Soup')
        recipe.save()
        ingredient = models.Ingredient(name='Tomato')
        ingredient.recipe = recipe
        ingredient.save()

        recipe2 = models.Recipe.objects.create(name='Tomato Soup')
        recipe2.save()
        ingredient2 = models.Ingredient(name='Tomato')
        ingredient2.recipe = recipe2
        ingredient2.save()

        self.assertNotEqual(ingredient.id, ingredient2.id)

    def test_same_name_same_recipe(self):
        """Test ingredients of the same name are not allowed to be created"""
        recipe = models.Recipe.objects.create(name='Tomato Soup')
        recipe.save()
        ingredient = models.Ingredient(name='Tomato')
        ingredient.recipe = recipe
        ingredient.save()

        ingredient2 = models.Ingredient(name='Tomato')
        ingredient2.recipe = recipe
        try:
            ingredient2.save()
            self.fail("unique_together condition is not being met.")
        except IntegrityError:
            pass
