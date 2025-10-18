from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        authenticated_user = authenticate(username=username,password=password)
        if authenticated_user is None:
            raise serializers.ValidationError(
                {
                    "detail":"Password is incorrect."
                }
            )
        return attrs

