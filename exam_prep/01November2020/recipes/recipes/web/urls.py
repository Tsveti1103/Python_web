from django.urls import path

from recipes.web.views import index, create, delete, details, edit

urlpatterns = (
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details'),
    path('edit/<int:pk>/', edit, name='edit'),
)
