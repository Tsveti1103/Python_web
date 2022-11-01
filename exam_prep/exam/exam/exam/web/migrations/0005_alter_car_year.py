# Generated by Django 3.2.16 on 2022-10-30 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1980, message='Year must be between 1980 and 2049'), django.core.validators.MaxValueValidator(2049, message='Year must be between 1980 and 2049')]),
        ),
    ]
