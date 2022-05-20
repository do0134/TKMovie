from rest_framework import serializers
from django.conf import settings
from ..models import Comment



# CUD => validation
# R => Data serializing
class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = settings.AUTH_USER_MODEL
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )
