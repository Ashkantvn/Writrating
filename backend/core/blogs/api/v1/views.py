from rest_framework.views import APIView
from blogs.api.v1.serializers import BlogListSerializer
from blogs.models import Blog
from rest_framework.response import Response
from rest_framework import status

class BlogListAPIView(APIView):
    
    def get(self,request):
        serializer = BlogListSerializer(Blog.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)