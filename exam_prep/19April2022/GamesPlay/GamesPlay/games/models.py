from django.core import validators
from django.db import models
from enum import Enum


# Create your models here.
class Profile(models.Model):
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    AGE_MIN_VALUE = 12

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validators.MinValueValidator(AGE_MIN_VALUE),),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name.strip()} {self.last_name.strip()}'
        elif self.first_name:
            return f'{self.first_name}'.strip()
        elif self.last_name:
            return f'{self.last_name}'.strip()
        return None


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    ACTION = 'Action'
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BORD_CARD = "Board/Card Game"
    OTHER = "Other"


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(RATING_MIN_VALUE),
            validators.MaxValueValidator(RATING_MAX_VALUE),),
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(LEVEL_MIN_VALUE),
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)
