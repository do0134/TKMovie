from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('get_movies/', views.get_movie_datas),
]
