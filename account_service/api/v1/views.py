from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.serializers import VerifyAccessTokenSerializer

class Logout(APIView):
    pass

class SignUp(APIView):
    pass

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