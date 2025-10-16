from rest_framework.views import APIView
from api.v1.serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

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
                    "access_token": str(access_token),
                    "refresh_token": str(refresh_token)
                }
            },
            status=status.HTTP_201_CREATED
        )