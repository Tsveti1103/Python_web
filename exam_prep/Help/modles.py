from enum import Enum
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# if we have choices:
class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


class Album(models.Model):
    GENRE_MAX_LENGTH = 30

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        # add validators. Here I can add and my validators:
        validators=(MinValueValidator(0.0),)
    )

    # the albums will be ordering always by pk. If not the ordering will change when edit some album
    class Meta:
        ordering = ('pk',)
