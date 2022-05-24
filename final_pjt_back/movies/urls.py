from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('get_movies/', views.get_movie_datas),
    path('<int:movie_pk>/',views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('movie_worldcup/',views.movie_worldcup),
    # comments
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
]
