from rest_framework import serializers
from ..models import Genre, Movie
from .review import ReviewSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class MovieSerializer(serializers.ModelSerializer): 
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class GenreSerializer(serializers.ModelSerializer):
        class Meta : 
            model = Genre
            fields = '__all__'
    
    reviews = ReviewSerializer(many=True, read_only=True)

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
    user = UserSerializer(read_only=True)
    class Meta : 
        model = Movie
        fields = ('pk','title','poster_path','user')


# class MovieListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username')

#     user = UserSerializer(read_only=True)
#     # queryset annotate (views에서 채워줄것!)
#     comment_count = serializers.IntegerField()
#     like_count = serializers.IntegerField()

#     class Meta:
#         model = Article
#         fields = ('pk', 'user', 'title', 'comment_count', 'like_count','created_at')
