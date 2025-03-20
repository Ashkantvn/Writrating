from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.models import Profile
from blogs.models import Blog,Category,Tag
from django.db import transaction

class AuthorBlogSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username']

class CategoryBlogSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class TagBlogSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class BlogSerializer(ModelSerializer):
    author = AuthorBlogSerializer(read_only=True)
    categories = CategoryBlogSerializer(many=True, read_only=True)
    tags = TagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        exclude = ['update_date','create_date','publishable','status']


class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'title',
            'banner',
            'content',
            'status',
            'publishable',
            'categories',
            'tags',
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        author = getattr(request.user, 'profile', None)
        
        if not author:
            raise serializers.ValidationError(detail="A valid user profile is required to create a blog post.")
        
        categories = validated_data.pop('categories',[])
        tags = validated_data.pop('tags',[])

        with transaction.atomic():
            blog = Blog.objects.create(author=author, **validated_data)
            blog.categories.add(*categories)
            blog.tags.add(*tags)

        return blog
        
