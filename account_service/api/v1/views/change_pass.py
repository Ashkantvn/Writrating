from rest_framework.views import APIView
from api.v1.serializers import ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ChangePass(APIView, IsAuthenticated):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data
        )
        if not serializer.is_valid():
            return Response(
                data={"detail": serializer.errors.get("detail")[0]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"data": "Password changed."},
            status=status.HTTP_200_OK
        )
