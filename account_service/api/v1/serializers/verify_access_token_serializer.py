from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from api.models import AccessTokenBlacklist

class VerifyAccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()

    def validate(self, attrs):
        access_token = attrs.get("access_token")

        try:
            token = AccessToken(access_token)
            token.check_exp()
            jti = token.get("jti")

            if AccessTokenBlacklist.objects.filter(jti=jti).exists():
                raise serializers.ValidationError("Token has been blacklisted.")

        except TokenError:
            raise serializers.ValidationError("Invalid or expired token.")

        # If everything is fine, you can attach extra info to attrs
        attrs["jti"] = jti
        return attrs