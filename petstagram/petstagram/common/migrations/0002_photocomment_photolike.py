# Generated by Django 3.2.15 on 2022-10-20 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0003_alter_photo_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
    ]
