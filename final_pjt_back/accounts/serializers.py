from .models import User
from rest_framework import serializers
from articles.models import Article
class EachUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','username',)
class FollowerSerializer(serializers.ModelSerializer):
    followers = EachUserSerializer(many=True, read_only= True)
    following = EachUserSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('followers','following')

class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    followers = FollowerSerializer(many = True)
    following = FollowerSerializer(many = True)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'like_articles', 'articles','followers','following')