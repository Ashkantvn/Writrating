from rest_framework.serializers import ModelSerializer
from accounts.models import Profile
from blogs.models import Blog,Category,Tag


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

class BlogListSerializer(ModelSerializer):
    author = AuthorBlogSerializer(read_only=True)
    categories = CategoryBlogSerializer(many=True, read_only=True)
    tags = TagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        exclude = ['update_date','create_date','publishable','status']
