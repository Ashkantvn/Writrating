from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.v1.serializers import LogoutSerializer
from rest_framework.response import Response
from rest_framework import status
from api.models import AccessTokenBlacklist


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"detail": serializer.errors.get("detail")[0]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        access_token = serializer.validated_data["access_token_obj"]
        AccessTokenBlacklist.objects.create(jti=access_token.get("jti"))
        return Response(status=status.HTTP_204_NO_CONTENT)
