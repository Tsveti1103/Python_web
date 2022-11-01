from django.db import models


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        verbose_name='Last name',

    )
    image_url = models.URLField(
        verbose_name='Image URL',

    )


class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH,)
    description = models.TextField()
    image_url = models.URLField(verbose_name='Image',
)
    type = models.CharField(max_length=TYPE_MAX_LENGTH)
