from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    new_password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = ["new_password", "new_password_confirm"]

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")
        # Check password and password confirm are same
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                {"detail": "Password and password confirm mismatch."}
            )
        # Validate password
        try:
            validate_password(password=new_password)
        except ValidationError:
            raise serializers.ValidationError({"detail": "Weak password."})
        return attrs

    def update(self, instance, validated_data):
        new_password = validated_data.get("new_password")
        instance.set_password(new_password)
        instance.save()
        return instance
