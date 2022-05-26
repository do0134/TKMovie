from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ProfileSerializer
User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    temp = User.objects.all()
    idx = 0
    for i in range(len(temp)):
        if temp[i] == username:
            idx = i
            break
    user = User.objects.annotate(
        follower_count = Count('followers'),
        following_count = Count('following')
    ).all()[idx]

    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    
@api_view(['POST'])
def follow(request, username):

    temp = User.objects.all()
    idx = 0
    for i in range(len(temp)):
        if temp[i] == username:
            idx = i
            break
    person = User.objects.annotate(
        follower_count = Count('followers'),
        following_count = Count('following')
    ).all()[idx]
    print(person.username)
    if person.followers.filter(pk=request.user.pk).exists():
        person.followed = False
        person.followers.remove(request.user.pk)
        serializer = ProfileSerializer(person)

        return Response(serializer.data)
    else:
        person.followed = True
        person.followers.add(request.user.pk) 
        serializer = ProfileSerializer(person)

        return Response(serializer.data)      
        
        
