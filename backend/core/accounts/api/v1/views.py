from django.shortcuts import render
from accounts.api.v1.serializers import ProfileSerializer
from accounts.models.profile_model import Profile
from rest_framework.response import Response
from rest_framework import status , response, generics , mixins
from django.shortcuts import get_object_or_404
from accounts.api.v1.permissions import CustomIsAuthenticatedOrReadOnly

# Create your views here.
class ProfileAPI(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    """
        Profile api let users see users profile and edit their profile .
        Methods: GET , PATCH
    """
    permission_classes = [CustomIsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "username"

        
    def get(self,request,username,format=None):
        return self.retrieve(request=request)
    
    def patch(self,request,username,format=None,*args,**kwargs):
        profile = get_object_or_404(Profile,username=username)
        if  profile.user.email != request.user.email:
            return Response(data={"detail":"You can only change your profile"},status=status.HTTP_403_FORBIDDEN)
        return self.partial_update(request=request,*args,**kwargs)


class SignUpAPI(generics.GenericAPIView):
    pass

class LoginAPI(generics.GenericAPIView):
    pass

class LogoutAPI(generics.GenericAPIView):
    pass

class DeleteAccountAPI(generics.GenericAPIView):
    pass

class ChangePassAPI(generics.GenericAPIView):
    pass

class PasswordRecoveryAPI(generics.GenericAPIView):
    pass

class PasswordRecoveryVerificationAPI(generics.GenericAPIView):
    pass