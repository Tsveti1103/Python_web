from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music.web.validators import validate_only_alphanumeric


# Create your models here.
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


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_only_alphanumeric,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    album = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.0),)
    )

    class Meta:
        ordering = ('pk',)
