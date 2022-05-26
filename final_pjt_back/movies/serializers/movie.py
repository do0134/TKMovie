from rest_framework import serializers
from ..models import Genre, Movie, Review
from.review import ReviewSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class MovieSerializer(serializers.ModelSerializer): 
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)
    class GenreSerializer(serializers.ModelSerializer):
        class Meta : 
            model = Genre
            fields = '__all__'
    class MovieReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk','content', 'rating','user','movie')
            read_only_fields = ('user','movie')
    movie_review = MovieReviewSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True,read_only=True)
    movie_like_users = UserSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField()
    movie_rating = serializers.IntegerField()
    class Meta:
        model = Movie
        fields = '__all__'

class MovieWorldCupSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username')
    class GenreSerializer(serializers.ModelSerializer):
        class Meta : 
            model = Genre
            fields = '__all__'
    user = UserSerializer(read_only=True)
    class Meta : 
        model = Movie
        fields = '__all__'


class WorldcupWinner(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta : 
            model = User
            fields = ('pk',)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ('pk','user')

class MovieWinnerSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta : 
            model = Genre
            fields = '__all__'
    user = UserSerializer(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)
    win_worldcup = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Movie
        fields = ('pk', 'user', 'title', 'overview','poster_path','released_date','genres','win_worldcup')

class TopTen(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    win_worldcup = UserSerializer(read_only=True,many=True)
    win_cnt = serializers.IntegerField()
    class Meta:
        model = Movie
        fields = ('pk','title','overview','poster_path','win_worldcup','win_cnt')