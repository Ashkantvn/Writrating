from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class Login(APIView):
    def post(self,request):
        username=request.data.get("username")
        # Check user is exist
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                data={
                    "detail":"User not found."
                },
                status= status.HTTP_404_NOT_FOUND
            )
        serializer = LoginSerializer(data=request.data)
        # Check password is valid
        if not serializer.is_valid():
            return Response(
                data={
                    "detail":serializer.errors.get('detail')[0]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # Create jwt for user
        refresh_rate= RefreshToken.for_user(user)
        access_token= refresh_rate.access_token
        return Response(
            data={
                "data":{
                    "refresh_token": str(refresh_rate),
                    "access_token": str(access_token),
                }
            },
            status=status.HTTP_200_OK
        )
