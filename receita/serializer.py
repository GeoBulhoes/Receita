from rest_framework import serializers
from .models import Recipe

class RecipeSerializers(serializers.ModelSerializer):
	class Meta:
		models = Recipe
		fields = '__all__'
