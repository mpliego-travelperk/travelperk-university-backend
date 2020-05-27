from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core import models
from core.models import Recipe
from recipe.serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')


def add_ingredient_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-add-ingredient', args=[recipe_id])


def remove_ingredient_url(ingredient_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-remove-ingredient', args=[ingredient_id])


class RecipeViewTests(TestCase):
    """Recipe REST API Tests"""

    def setUp(self):
        self.client = APIClient()

    def test_read_recipe(self):
        """Test read of a recipe"""
        recipe = models.Recipe.objects.create(
            name='Recipe Read',
            description='Recipe Read Description'
        )
        recipe.save()
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
        recipe = models.Recipe.objects.create(
            name='Recipe Read',
            description='Recipe Read Description'
        )
        recipe.save()
        res = self.client.post(
            add_ingredient_url(recipe.id), {'name': 'Ingredient 1'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = self.client.post(
            add_ingredient_url(recipe.id), {'name': 'Ingredient 2'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
