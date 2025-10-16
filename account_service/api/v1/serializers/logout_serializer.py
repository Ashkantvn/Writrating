from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        access_token = attrs.get("access_token")
        refresh_token = attrs.get("refresh_token")
        try:
            AccessToken(access_token)
            RefreshToken(refresh_token)
        except TokenError:
            raise serializers.ValidationError({
                "detail":"Invalid token."
            })
        return attrs
