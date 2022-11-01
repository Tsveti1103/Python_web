# Generated by Django 3.2.16 on 2022-10-27 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('BORD_CARD', 'Board/Card Game'), ('OTHER', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(5.0)])),
                ('max_level', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]