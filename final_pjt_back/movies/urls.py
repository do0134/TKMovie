from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('get_movies/', views.get_movie_datas),
    path('<int:movie_pk>/',views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    
    # comments
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),

    #movie_worldcup
    path('movie_worldcup/',views.movie_worldcup),
    path('movie_worldcup/<int:movie_pk>/win/',views.get_worldcupwinner),
    path('movie_worldcup/<username>/recommend/',views.winner_base_recommend),
    path('movie_worldcup/topten/',views.top_ten),
    path('movie_worldcup/follower_like/<int:user_pk>',views.follower_like),
    path('movie_worldcup/<username>/', views.get_my_winner),
]
