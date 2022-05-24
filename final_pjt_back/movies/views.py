from django.shortcuts import render
import json
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Movie
from .serializers.movie import MovieSerializer
from django.shortcuts import get_object_or_404
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
    movie = get_object_or_404(Movie, pk=movie_pk)

    def movie_detail():
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'GET':
        return movie_detail()
