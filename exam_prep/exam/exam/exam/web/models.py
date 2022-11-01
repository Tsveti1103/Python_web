from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    MIN_USERNAME_LENGTH = 2
    MIN_AGE_VALUE = 18
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[validators.MinLengthValidator(MIN_USERNAME_LENGTH)],
        error_messages={
            'min_length': 'The username must be a minimum of 2 chars'
        })
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(MIN_AGE_VALUE)]
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


class CarType(ChoicesEnum):
    SPORTS = 'Sports Car'
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    PRICE_MIN_VALUES = 1
    YEAR_MIN_VALUES = 1980
    YEAR_MAX_VALUES = 2049

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        null=False,
        blank=False,
        choices=CarType.choices()
    )
    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[validators.MinLengthValidator(MODEL_MIN_LENGTH)]
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(YEAR_MIN_VALUES, message='Year must be between 1980 and 2049'),
                    validators.MaxValueValidator(YEAR_MAX_VALUES, message='Year must be between 1980 and 2049')],
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1.0)]
    )
