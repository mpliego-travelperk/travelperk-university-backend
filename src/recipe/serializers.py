from rest_framework import serializers
from core.models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    """Serialize an ingredient"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id', 'name', 'description', 'ingredients'
        )
        read_only_fields = ('id', 'ingredients')
