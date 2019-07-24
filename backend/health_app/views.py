from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import Profile, Extracted_data, Original_image 
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OriginalSerializer,ProfileSerializer, ExtractedSerializer,UserSerializer

# * serializing the Django User model
class UserList(APIView):

    #* api for getting all users
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)
    
    #* creating new user api
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# * serializing the Profile objects
class ProfileList(APIView):

    # * creating api to get all profile objects as json
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    
    # * function to add a new object in the models via the API
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class OriginalList(APIView):
    def get(self, request, format=None):
        all_originals = Original_image.objects.all()
        serializers = OriginalSerializer(all_originals,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = OriginalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)   

class ExtractedList(APIView):
    def get(self, request, format=None):
        all_extracts = Extracted_data.objects.all()
        serializers = ExtractedSerializer(all_extracts,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ExtractedSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
