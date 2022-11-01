from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def validate_ingredients(value):
    if ',' not in value:
        raise ValidationError('The ingredients should be separated by ",".')


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=INGREDIENTS_MAX_LENGTH, validators=(validate_ingredients,), )
    time = models.IntegerField()
