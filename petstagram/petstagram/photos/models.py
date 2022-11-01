from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


# Create your models here.

class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        null=False,
        blank=True,
        validators=(validate_file_size,)
    )

    description = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Automatically sets current date on save (on update or create)
        auto_now=True,
        blank=False,
        null=True,

    )

    tagged_pets = models.ManyToManyField(
        Pet,
        null=True,
    )
