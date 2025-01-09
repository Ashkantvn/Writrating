from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

User =  get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        fields = [
            "id",
            "username",
            "profile_image",
            "first_name",
            "last_name",
            "description",
        ]
        read_only_fields = ["id"]

    def validate_username(self, value):
        invalid_chars = set("!@#$%^&*()+=[]{}|\\:;\"'<>,.?/")
        if " " in value:
            raise serializers.ValidationError("Username should not contain spaces")
        elif any(char in invalid_chars for char in value):
            raise serializers.ValidationError("Username contains invalid characters")
        else:
            return value
        

class SignUpSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True,max_length=128)

    class Meta:
        model = User
        fields = ["email","password","password_confirm"]

    def validate_email(self,value):
        try:
            validate_email(value=value)
        except serializers.ValidationError as validationError:
            raise validationError({"detail":"Email validation failed."})
        if User.objects.filter(email=value).exists() :
            raise serializers.ValidationError({"detail":"Email address already in use"})
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"detail":"password and password confirm must match."})
        return data
    
    def create(self,validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
