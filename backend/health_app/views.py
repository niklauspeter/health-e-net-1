from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile, Extracted_data, Original_image 
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OriginalSerializer,ProfileSerializer, ExtractedSerializer,UserSerializer

class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)
        
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class OriginalList(APIView):
    def get(self, request, format=None):
        all_originals = Original_image.objects.all()
        serializers = OriginalSerializer(all_originals,many=True)
        return Response(serializers.data)

class ExtractedList(APIView):
    def get(self, request, format=None):
        all_extracts = Extracted_data.objects.all()
        serializers = ExtractedSerializer(all_extracts,many=True)
        return Response(serializers.data)
