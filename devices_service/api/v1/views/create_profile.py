from rest_framework.views import APIView
from api.permissions import IsSuperUser
from api.v1.serializers import CreateProfileSerializer
from rest_framework.response import Response
from rest_framework import status

class CreateProfile(APIView):
    permission_classes = [IsSuperUser]

    def post(self,request):
        serializer= CreateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={
            "data":"Profile created successfully."
            },
            status=status.HTTP_201_CREATED
        )