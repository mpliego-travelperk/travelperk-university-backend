from django.db import IntegrityError
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.models import Recipe, Ingredient
from recipe import serializers


class IngredientViewSet(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """Manage ingredients in the database"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'add_ingredient':
            return serializers.IngredientSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='add-ingredient')
    def add_ingredient(self, request, pk=None):
        """Adds a new ingredient"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            data=request.data
        )
        if serializer.is_valid():
            try:
                serializer.save(recipe=recipe)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except IntegrityError:
                return Response(
                    status=status.HTTP_409_CONFLICT
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
