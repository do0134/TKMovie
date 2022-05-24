from rest_framework import serializers
from ..models import Review

from django.contrib.auth import get_user_model
User = get_user_model()

# CUD => validation
# R => Data serializing

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie',)
        read_only_fields = ('movie', )
