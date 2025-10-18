from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class StatelessUser:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.is_authenticated = True


class StatelessJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id")
        username = validated_token.get("username")

        if not user_id or not username:
            raise InvalidToken("Missing user_id or username in token")

        # Create a lightweight user-like object
        user = StatelessUser(user_id, username)
        return user
