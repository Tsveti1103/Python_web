from django.urls import path, include

from GamesPlay.games.views import index, dashboard, create_game, delete_game, details_game, edit_game, create_profile, \
    delete_profile, details_profile, edit_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', create_game, name='create game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
        path('details/<int:pk>/', details_game, name='details game'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
    ]))
)
