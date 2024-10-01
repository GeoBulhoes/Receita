#from django.shortcuts import render
from rest_framework import viewsets
from receita.models import Recipe
from .serializer import RecipeSerializers

# Create your views here.

class ReceitaViewSet(viewsets.ModelViewSet):
	'''Exibir todas as receitas'''
	queryset = Recipe.objects.all()
	Serializer_class = RecipeSerializers
