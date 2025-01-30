import pytest
from blogs.models.blogs_model import Blog
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def blog():
    author = User.objects.create(
        email = 'test323123@example.com',
        password = "ewoacmoijsdoj@234",
        is_active = True,
        is_admin = True,
    )
    fake_blog = Blog.objects.create(
        title='Test Blog', 
        content='Test Content',
        author=author.profile,
        )
    yield fake_blog
    if fake_blog.pk:
        fake_blog.delete()
    author.delete()

@pytest.fixture
def blog_with_more_than_60_characters():
    author = User.objects.create(
        email = 'test323123@example.com',
        password = "ewoacmoijsdoj@234",
        is_active = True,
        is_admin = True,
    )
    fake_blog = Blog.objects.create(
        title='blog title' * 60,
        content='Test Content',
        author=author.profile,
    )
    yield fake_blog
    author.delete()

@pytest.fixture
def blog_with_blank_fields():
    author = User.objects.create(
        email = 'test323123@example.com',
        password = "ewoacmoijsdoj@234",
        is_active = True,
        is_admin = True,
    )
    fake_blog = Blog.objects.create(
        title='',
        content='',
        author=author.profile,
    )
    yield fake_blog
    author.delete()