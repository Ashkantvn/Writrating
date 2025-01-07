from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile

        fields = ["id","username","profile_image","first_name","last_name","description"]
        read_only_fields = ["id"]

    def validate_username(self,value):
        invalid_chars = set('!@#$%^&*()+=[]{}|\\:;"\'<>,.?/')
        if " " in value:
            raise serializers.ValidationError("Username should not contain spaces")
        elif any(char in invalid_chars for char in value):
            raise serializers.ValidationError("Username contains invalid characters")
        else:
            return value