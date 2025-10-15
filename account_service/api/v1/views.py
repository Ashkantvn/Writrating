from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.serializers import (
    VerifyAccessTokenSerializer,
    SignUpSerializer
)
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class Logout(APIView):
    pass

class SignUp(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    "detail":serializer.errors["detail"][0]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = serializer.save()
        # Create refresh and access tokens
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        return Response(
            data={
                "data":{
                    "access": str(access_token),
                    "refresh": str(refresh_token)
                }
            },
            status=status.HTTP_201_CREATED
        )
        

class VerifyAccessToken(APIView):
    def post(self, request):
        access_token= request.data.get("access_token")
        serializer = VerifyAccessTokenSerializer(
            data={
                "access_token":access_token
            }
        )
        if serializer.is_valid():
            return Response(
                data={
                    "data": serializer.validated_data["access_token"]
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "detail": "Invalid token."
                },
                status=status.HTTP_400_BAD_REQUEST
            )