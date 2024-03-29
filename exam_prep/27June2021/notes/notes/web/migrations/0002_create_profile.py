# Generated by Django 3.2.16 on 2022-10-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
