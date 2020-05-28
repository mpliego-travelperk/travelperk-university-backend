from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core import models
from core.models import Recipe, Ingredient
from recipe.serializers import RecipeSerializer, IngredientSerializer

RECIPE_URL = reverse('recipe:recipe-list')
INGREDIENT_URL = reverse('recipe:ingredient-list')


def ingredient_detail_url(ingredient_id):
    """Return ingredient URL"""
    return reverse('recipe:ingredient-detail', args=[ingredient_id])


def add_ingredient_url(recipe_id):
    """Return recipe add ingredient URL"""
    return reverse('recipe:recipe-add-ingredient', args=[recipe_id])


def sample_recipe(name='Recipe Read',
                  description='Recipe Read Description'):
    """Creates and persists a sample Recipe"""
    recipe = models.Recipe.objects.create(
        name=name,
        description=description
    )
    recipe.save()
    return recipe


class IngredientViewTests(TestCase):
    """Ingredient REST API Tests"""

    def setUp(self):
        self.client = APIClient()

    def test_read_ingredient(self):
        """Test read of a ingredient"""
        recipe = sample_recipe()
        ingredient = Ingredient.objects.create(
            name="Ingredient", recipe=recipe)
        res = self.client.get(INGREDIENT_URL)
        serializer = IngredientSerializer([ingredient], many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_remove_ingredient(self):
        """Test remove an ingredient"""
        recipe = sample_recipe()
        ingredient = Ingredient.objects.create(
            name='Ingredient', recipe=recipe)
        ingredient.save()
        res = self.client.delete(ingredient_detail_url(ingredient.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class RecipeViewTests(TestCase):
    """Recipe REST API Tests"""

    def setUp(self):
        self.client = APIClient()

    def test_read_recipe(self):
        """Test read of a recipe"""
        recipe = sample_recipe()
        res = self.client.get(RECIPE_URL)
        serializer = RecipeSerializer([recipe], many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_recipe(self):
        """Test create of a recipe"""
        payload = {
            'name': 'Recipe Create',
            'description': 'Recipe Create Description',
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_add_ingredients(self):
        """Test creating recipe with ingredients"""
        recipe = sample_recipe()
        res = self.client.post(
            add_ingredient_url(recipe.id), {'name': 'Ingredient 1'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = self.client.post(
            add_ingredient_url(recipe.id), {'name': 'Ingredient 2'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
