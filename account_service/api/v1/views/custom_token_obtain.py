from rest_framework_simplejwt.views import TokenObtainPairView
from api.v1.serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer