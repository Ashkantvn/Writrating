from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
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
            raise serializers.ValidationError(
                {"detail": "Password and password confirm mismatch."}
            )
        # Check password
        try:
            validate_password(password=password)
        except ValidationError:
            raise serializers.ValidationError({"detail": "Weak password."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        user = User.objects.create_user(**validated_data)
        return user
