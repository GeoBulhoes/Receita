from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    PUBLIC_PRIVATE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(null=False, blank=False)  # Lista de ingredientes como texto
    preparation = models.TextField()  # Modo de preparo
    preparation_time = models.PositiveIntegerField()  # Tempo em minutos
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Relacionamento com Category
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com User
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    visibility = models.CharField(max_length=7, choices=PUBLIC_PRIVATE_CHOICES, default='public')  # Público ou Privado

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')  # Relacionamento com Recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com User
    score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Nota de 1 a 5
    comment = models.TextField(blank=True, null=True)  # Comentário opcional

    def __str__(self):
        return f'{self.user} - {self.recipe} - {self.score}'
