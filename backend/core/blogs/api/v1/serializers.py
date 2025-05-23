from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, exceptions
from accounts.models import Profile
from blogs.models import Blog, Category, Tag, BlogResponse
from django.db import transaction


class AuthorBlogSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username"]


class CategoryBlogSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TagBlogSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class BlogSerializer(ModelSerializer):
    author = AuthorBlogSerializer(read_only=True)
    categories = CategoryBlogSerializer(many=True, read_only=True)
    tags = TagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        exclude = ["update_date", "create_date", "publishable", "status"]


class BlogCreateAndEditSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "title",
            "banner",
            "content",
            "status",
            "publishable",
            "categories",
            "tags",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        author = getattr(request.user, "profile", None)

        if not author:
            raise serializers.ValidationError(
                detail="A valid user profile is required to create a blog post."
            )

        categories = validated_data.pop("categories", [])
        tags = validated_data.pop("tags", [])

        # Insure that block of code executed within db transactions
        with transaction.atomic():
            blog = Blog.objects.create(author=author, **validated_data)
            blog.categories.add(*categories)
            blog.tags.add(*tags)

        return blog


class BlogCheckSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = [
            "id",
            "title",
            "banner",
            "content",
            "status",
            "views",
            "author",
            "tags",
            "categories",
            "slug",
            "published_date",
            "update_date",
            "create_date",
        ]

    def validate(self, attrs):
        """
        Enshure that only publishable field is editable
        """
        allowed_fields = ["publishable"]
        extra_fields = set(attrs.keys()) - set(allowed_fields)
        if (extra_fields) or (allowed_fields[0] not in attrs.keys()):
            raise exceptions.PermissionDenied(
                detail="You can only edit publishable field."
            )
        return super().validate(attrs)

    def update(self, instance, validated_data):
        """
        Update only publishable field
        """
        instance.publishable = validated_data.get("publishable", instance.publishable)
        instance.save()
        return instance


class ResponseSerializer(ModelSerializer):
    class Meta:
        model = BlogResponse
        fields = ["title", "content"]

    def create(self, validated_data):
        """
        Set the author of the blog as response_to value, and set the response author.
        """
        blog_author = self.context.get("blog_author")
        user = self.context.get("user")
        author = getattr(user, "profile", None)
        if not blog_author or not author:
            raise serializers.ValidationError(
                detail="A valid user profile is required to create a blog response."
            )

        response = BlogResponse.objects.create(
            response_to=blog_author, author=author, **validated_data
        )
        response.save()

        return response
