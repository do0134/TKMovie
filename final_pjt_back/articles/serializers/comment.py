from rest_framework import serializers

from ..models import Comment
from django.contrib.auth import get_user_model


User = get_user_model()



# CUD => validation
# R => Data serializing
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )
