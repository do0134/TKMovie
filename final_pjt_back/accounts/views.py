from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ProfileSerializer


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    
@api_view(['POST'])
def follow(request, user_pk):
    if request.user.is_authenticated:
        #좋아요 상태라면 > 좋아요 취소
        #아무것도 안했으면 > 좋아요
        person = get_object_or_404(User, pk=user_pk)
        if person.followers.filter(pk=request.user.pk).exists():
            followed = False
            person.followers.remove(request.user.pk)
        else:
            followed = True
            person.followers.add(request.user.pk)
            
        context = {
            'followed': followed,
            'count' : person.followers.count(),
        }
        return JsonResponse(context)
    return JsonResponse({'logined': False})

