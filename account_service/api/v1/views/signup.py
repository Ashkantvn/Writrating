from rest_framework.views import APIView
from api.v1.serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status


class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"detail": serializer.errors["detail"][0]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        # Create refresh and access tokens
        return Response(
            data={"data": "User created successfully."},
            status=status.HTTP_201_CREATED
        )
