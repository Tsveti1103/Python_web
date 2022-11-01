from django.urls import path

from demos_and_tests.tasks import views

urlpatterns = [
    path('', views.index)
]