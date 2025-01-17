from accounts.api.v1.serializers import ProfileSerializer, SignUpSerializer, ChangePasswordSerializer
from accounts.models.profile_model import Profile

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response
from rest_framework import status, generics, mixins, permissions
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
class ProfileAPI(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin
):
    """
        Profile api let users see users profile and edit their profile .
        Methods: GET , PATCH
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "username"

    def get(self, request, username, format=None):
        return self.retrieve(request=request)

    def patch(self, request, username, format=None, *args, **kwargs):
        profile = get_object_or_404(Profile, username=username)
        if profile.user.pk != request.user.id:
            return Response(
                data={"detail": "You can only change your profile"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return self.partial_update(request=request, *args, **kwargs)


class SignUpAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    """
        Sign-up api let users signup to website.
        Method: POST
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh_token = RefreshToken.for_user(user)
        response_data = {
            "user": serializer.data["email"],
            "token_access": str(refresh_token.access_token),
            "refresh_token": str(refresh_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LogoutAPI(APIView):
    """
        Log out API let users logout from their accounts
        Method: POST
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            access_token = request.data["access_token"]

            refresh_token = RefreshToken(refresh_token)
            refresh_user_id = refresh_token.payload.get("user_id")

            access_token = AccessToken(access_token)
            access_user_id = access_token.payload.get("user_id")

            if refresh_user_id != access_user_id:
                return Response(
                    {
                        "detail": "User mismatch for tokens."
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            if request.user.id != refresh_user_id:
                return Response(
                    {"detail": "This token does not belong to you"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            refresh_token.blacklist()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except TokenError:
            return Response(
                data={"detail": "Token error"}, status=status.HTTP_400_BAD_REQUEST
            )


class DeleteAccountAPI(APIView):
    """
        Delete account API let users delete their accounts
        Method: DELETE
    """
    permission_classes= [permissions.IsAuthenticated]

    def delete(self,request,*args,**kwargs):
            user = get_object_or_404(User,pk=request.user.id)
            user.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)


class ChangePassAPI(APIView):
    """
        Change password API let users change their password
        Method: PATCH
    """
    
    permission_classes = [permissions.IsAuthenticated,]

    def patch(self,request,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={"request": request})
        if serializer.is_valid(raise_exception=True):
            # Update user's password
            user = request.user
            user.set_password(serializer._validated_data["new_password"])
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PasswordRecoveryAPI(generics.GenericAPIView):
    pass


class PasswordRecoveryVerificationAPI(generics.GenericAPIView):
    pass
