from django.shortcuts import render
import json
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review
from .serializers.movie import MovieSerializer, ReviewSerializer, MovieWorldCupSerializer,WorldcupWinner
from django.shortcuts import get_object_or_404
from django.db.models import Count,Avg
from rest_framework import status
import random
# Create your views here.

TMDB_API_KEY = '38fb6be42c82ed986f17fb3d9195b8bc'

def get_movie_datas():
    if False:
        total_data = []
        # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
        for i in range(1, 50):
            request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
            movies = requests.get(request_url).json()
            print(i)
            for movie in movies['results']:
                if movie.get('release_date', ''):
                    fields = {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'released_date': movie['release_date'],
                        'popularity': movie['popularity'],
                        'vote_avg': movie['vote_average'],
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids']
                    }

                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields
                    }

                    total_data.append(data)

        with open("movie_data.json",  encoding="UTF-8"):
            json.dump(total_data, indent="\\t", ensure_ascii=False)

#get_movie_datas()

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.annotate(
        review_count = Count('review'),
        movie_rating = Avg('review__rating')
    ).get(pk=movie_pk)
    def movie_detail():
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'GET':
        return movie_detail()

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.movie_like.filter(pk=user.pk).exists():
        movie.movie_like.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.movie_like.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie, user=user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    
    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

@api_view(['GET'])
def movie_worldcup(request):
    movies = Movie.objects.all()
    ran_num = [_ for _ in range(967)]
    idx = random.sample(ran_num,16)
    
    worldcup_list = []
    
    for i in idx:
        worldcup_list.append(movies[i])
    
    serializer = MovieWorldCupSerializer(worldcup_list,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def get_worldcupwinner(request,movie_pk):
    movie = get_object_or_404(Movie,pk = movie_pk)
    user = request.user
    if movie.win_worldcup.filter(pk=user.pk).exists():

        serializer = WorldcupWinner(movie)
        return Response(serializer.data)
    else:

        movie.win_worldcup.add(user)
        serializer = WorldcupWinner(movie)
        return Response(serializer.data)

