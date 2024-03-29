# Generated by Django 3.2.16 on 2022-10-30 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20221030_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(error_messages={'max_value_validator': 'Year must be between 1980 and 2049', 'min_value_validator': 'Year must be between 1980 and 2049'}, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2049)]),
        ),
    ]
