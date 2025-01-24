from rest_framework import serializers

from accounts.models import Profile
from accounts.api.v1.exceptions import PermissionDeniedException

from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from accounts.models import RecoveryCode

User = get_user_model()


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
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password_confirm"]

    def validate_email(self, value):
        try:
            validate_email(value=value)
        except serializers.ValidationError as validationError:
            raise validationError({"detail": "Email validation failed."})
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"detail": "Email address already in use"}
            )
        return value

    def validate(self, data):
        user = self.context["request"].user

        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError(
                {"detail": "password and password confirm must match."}
            )

        try:
            validate_password(data["password"], user=user)
        except ValidationError as error:
            raise serializers.ValidationError(detail={"password": list(error.messages)})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context["request"].user

        if not user.check_password(data["old_password"]):
            raise PermissionDeniedException(detail="Incorrect old password. ")

        if data["new_password"] != data["new_password_confirm"]:
            raise PermissionDeniedException(
                detail="Password and password confirm must match. "
            )

        try:
            validate_password(data["new_password"], user=user)
        except ValidationError as error:
            raise serializers.ValidationError(detail={"detail": list(error.messages)})

        return data


class PasswordRecoveryValidationSerialiaer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = RecoveryCode
        fields = ["email", "digits", "new_password", "new_password_confirm"]

    def validate_email(self, value):
        try:
            validate_email(value=value)
        except serializers.ValidationError as validationError:
            raise validationError({"detail": "Email validation failed."})
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError({"detail": "Email address not found"})
        return value

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as validationError:
            raise validationError({"detail": "Password validation failed."})
        return value

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {"detail": "password and password confirm must match."}
            )
        return super().validate(attrs)
