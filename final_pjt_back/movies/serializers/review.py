from rest_framework import serializers
from django.conf import settings
from ..models import Review



# CUD => validation
# R => Data serializing
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = settings.AUTH_USER_MODEL
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie',)
        read_only_fields = ('movie', )
