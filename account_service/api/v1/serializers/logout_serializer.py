from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from api.models import AccessTokenBlacklist

class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        access_token_str = attrs.get("access_token")
        refresh_token_str = attrs.get("refresh_token")
        try:
            access_token = AccessToken(access_token_str)
            refresh_token = RefreshToken(refresh_token_str)
            access_token.check_exp()
            refresh_token.check_exp()

            _=access_token.payload
            _=refresh_token.payload

            jti = access_token.get("jti")
            if AccessTokenBlacklist.objects.filter(jti=jti).exists():
                raise serializers.ValidationError({"detail":"Invalid token."})
            
        except TokenError:
            raise serializers.ValidationError({
                "detail":"Invalid token."
            })
        attrs["access_token_obj"] = access_token
        return attrs
