from django.urls import path
from GameApp import views

urlpatterns = [
    path('', views.index, name='gameapp_index'),
    path('about/',views.about,name ='gameapp_about'),
    path('snake/',views.snake,name='gameapp_snake'),
    path('pong/',views.pong,name='gameapp_pong'),
    path('ttt/',views.ttt,name='gameapp_ttt'),
    ]