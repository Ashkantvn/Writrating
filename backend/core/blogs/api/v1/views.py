from rest_framework.views import APIView
from blogs.api.v1.serializers import BlogSerializer, BlogCreateSerializer
from blogs.models import Blog
from rest_framework.response import Response
from rest_framework import status, permissions
from blogs.api.v1.permissions import IsAuthenticatedAndAdmin
import re

class BlogListAPIView(APIView):
    
    def get(self,request):
        serializer = BlogSerializer(Blog.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class BlogRetrieveAPIView(APIView):
    
    def get(self,request,slug):
        pattern = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
        if not re.match(pattern=pattern,string=slug):
            return Response(data={'detail':'Your slug is invalid'},status=status.HTTP_400_BAD_REQUEST)
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response(data={'detail':'Blog not found!'} ,status= status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class BlogAddAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]
    
    def post(self,request):
        serializer = BlogCreateSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"data":"Blog generated successfully"},status=status.HTTP_201_CREATED)
