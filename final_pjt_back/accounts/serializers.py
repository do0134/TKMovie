from .models import User
from rest_framework import serializers
from articles.models import Article

class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'like_articles', 'articles',)