from django.contrib import admin

from demos_and_tests.tasks.models import Task

# Register your models here.
admin.site.register(Task)
