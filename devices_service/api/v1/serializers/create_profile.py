from rest_framework import serializers
from api.models import Profile

class CreateProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['username']