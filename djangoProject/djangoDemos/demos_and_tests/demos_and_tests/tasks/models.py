from django.db import models


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()
