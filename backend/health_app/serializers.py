from rest_framework import serializers
from .models import Profile, Original_image, Extracted_data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name','last_name','gender','position','bio','pic','work_id','hospital_name')

class OriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Original_image
        fields = ('id','image','sickness')

class ExtractedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','age','contents')