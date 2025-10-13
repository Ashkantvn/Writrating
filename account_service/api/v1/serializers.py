from rest_framework import serializers
from api.models import AccessTokenBlacklist
from rest_framework_simplejwt.tokens import AccessToken, TokenError

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
        attrs["user_id"] = token.get("user_id")
        return attrs