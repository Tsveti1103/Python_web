# Generated by Django 3.2.16 on 2022-10-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=50)),
                ('task_text', models.TextField()),
            ],
        ),
    ]
