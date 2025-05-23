from rest_framework.views import APIView
from blogs.api.v1.serializers import (
    ResponseSerializer,
    BlogSerializer,
    BlogCreateAndEditSerializer,
    BlogCheckSerializer,
)
from blogs.models import Blog
from rest_framework.response import Response
from rest_framework import status
from core.permissions import IsAuthenticatedAndAdmin, IsAuthor, IsValidator
from django.shortcuts import get_object_or_404
import re


class BlogListAPIView(APIView):

    def get(self, request):
        serializer = BlogSerializer(Blog.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogRetrieveAPIView(APIView):

    def get(self, request, slug):
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogAddAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin]

    def post(self, request):
        serializer = BlogCreateAndEditSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"data": "Blog generated successfully"}, status=status.HTTP_201_CREATED
        )


class BlogEditAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin, IsAuthor]

    def patch(self, request, slug):
        """
        Update a blog post.
        """
        # Check if the slug is valid
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog = get_object_or_404(Blog, slug=slug)

        # Enfore object level permission
        self.check_object_permissions(request=request, obj=blog)

        serializer = BlogCreateAndEditSerializer(
            blog, data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={"data": "successfully updated."}, status=status.HTTP_200_OK
        )


class BlogDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedAndAdmin, IsAuthor]

    def delete(self, request, slug):
        """
        Delete a blog post
        """
        # Check if the slug is valid
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog = get_object_or_404(Blog, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=blog)

        blog.delete()

        return Response(
            data={"data": "successfully deleted."}, status=status.HTTP_200_OK
        )


class BlogCheckAPIView(APIView):
    permission_classes = [IsValidator]

    def get(self, request, slug):
        """
        Get target blog post to check if it is valid.
        """

        # Check if the slug is valid
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog = get_object_or_404(Blog, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=blog)

        serializer = BlogCheckSerializer(blog)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, slug):
        """
        Make blog post publishable, when it is.
        """

        # Check if the slug is valid
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog = get_object_or_404(Blog, slug=slug)

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=blog)

        serializer = BlogCheckSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={"data": "successfully updated."}, status=status.HTTP_200_OK
        )

    def post(self, request, slug):
        """
        Post reason of rejection.
        """
        # Check if the slug is valid
        pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
        if not re.match(pattern=pattern, string=slug):
            return Response(
                data={"detail": "Your slug is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog = get_object_or_404(Blog, slug=slug)
        blog_author = blog.author

        # Enforce object level permission
        self.check_object_permissions(request=request, obj=blog)

        serializer = ResponseSerializer(
            data=request.data,
            context={"user": request.user, "blog_author": blog_author},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={"data": "Response successfully sent"}, status=status.HTTP_200_OK
        )
