# Generated by Django 3.2.16 on 2022-10-29 10:22

from django.db import migrations, models
import recipes.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_create_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=250, validators=[recipes.web.models.validate_ingredients]),
        ),
    ]