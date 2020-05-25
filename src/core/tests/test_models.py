from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_new_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient(name="Tomato")

        self.assertEqual(str(ingredient), ingredient.name)

    def test_new_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe(
            name="Tomato Sauce",
            description="Tomato Sauce Description")

        self.assertEqual(str(recipe), recipe.name)

    def test_same_name_different_ingredient(self):
        ingredient = models.Ingredient(name="Tomato")
        ingredient.save()

        ingredient2 = models.Ingredient(name="Tomato")
        ingredient2.save()

        self.assertNotEqual(ingredient.id, ingredient2.id)
