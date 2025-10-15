from rest_framework import serializers
from api.models import AccessTokenBlacklist
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

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
    
class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ["username", "password", "password_confirm"]

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")
        user_exist = User.objects.filter(username=username).exists()
        # Check if user is exist
        if user_exist:
            raise serializers.ValidationError({"detail": "User exists."})
        # Check password and password confirm are the same
        if password != password_confirm:
            raise serializers.ValidationError({
                "detail":"Password and password confirm mismatch."
            })
        # Check password
        try:
            validate_password(password=password)
        except ValidationError:
            raise serializers.ValidationError({
                "detail":"Weak password."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return super().create(validated_data)

