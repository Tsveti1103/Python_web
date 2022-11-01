from django.db import models


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, verbose_name='First Name', )
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, verbose_name='Last Name')
    age = models.IntegerField()
    image_url = models.URLField(verbose_name='Link to Profile Image')


class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    image_url = models.URLField(verbose_name='Link to Image')
    content = models.TextField()

    class Meta:
        ordering = ('pk',)
