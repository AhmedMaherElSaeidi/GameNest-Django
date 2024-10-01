from django.db import models
from categories.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    url = models.CharField(max_length=250, null=True)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    price = models.FloatField(validators=[MinValueValidator(0)])
    downloads = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    image = models.ImageField(upload_to="games/", null=True)
    categories = models.ManyToManyField(
        Category, related_name="game_categories", blank=True
    )

    def __str__(self):
        return self.name
