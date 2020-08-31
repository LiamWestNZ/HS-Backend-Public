import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import get_user_model
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from ..models import Profile
from ..serializers import ProfileSerializer, ProfileUpdateSerializer


User = get_user_model()


@api_view(['GET'])
def profile_detail_api_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found"}, status=404)
    profile_obj = qs.first()
    serializer = ProfileSerializer(instance=profile_obj, context={"request": request})
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def profile_update_api_view(request, username, *args, **kwags):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found"}, status=404)
    profile_obj = qs.first()
    if request.method =='PUT':
        serializer = ProfileUpdateSerializer(instance=profile_obj, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Changes made successfully"
            return Response(data=data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

