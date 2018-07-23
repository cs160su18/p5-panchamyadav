from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('game', views.game, name='game'),
    path('score', views.score, name='score'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('authenticate', views.authenticate, name='authenticate')
]