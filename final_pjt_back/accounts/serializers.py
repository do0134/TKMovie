from rest_framework import serializers
from articles.models import Article
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    follower_count = serializers.IntegerField()
    following_count = serializers.IntegerField()
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'like_articles', 'articles','followers','following','follower_count','following_count')
