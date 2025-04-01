import pytest
from blogs.models.blogs_model import Blog
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from blogs.models import BlogResponse

User = get_user_model()


@pytest.fixture
def authenticated_admin_client():
    user = User.objects.create(
        email="test12431@test.com",
        password="testaofejioj!@##$#%234234",
        is_active=True,
        is_admin=True,
    )
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    user.delete()


@pytest.fixture
def authenticated_validator_client():
    user = User.objects.create(
        email="test125324235@test.com",
        password="aoiwemhoijmawfj234@#",
        is_validator=True,
        is_active=True,
    )
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    user.delete()


@pytest.fixture
def authenticated_user_client():
    user = User.objects
    user = User.objects.create(
        email="test12431@test.com",
        password="testaofejioj!@##$#%234234",
        is_active=True,
        is_admin=False,
    )
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    user.delete()


@pytest.fixture
def blog():
    author = User.objects.create(
        email="test323123@example.com",
        password="ewoacmoijsdoj@234",
        is_active=True,
        is_admin=True,
    )
    fake_blog = Blog.objects.create(
        title="Test Blog",
        content="Test Content",
        author=author.profile,
    )
    yield fake_blog
    if fake_blog.pk:
        fake_blog.delete()
    author.delete()


@pytest.fixture
def blog_with_more_than_60_characters():
    author = User.objects.create(
        email="test323123@example.com",
        password="ewoacmoijsdoj@234",
        is_active=True,
        is_admin=True,
    )
    fake_blog = Blog.objects.create(
        title="blog title" * 60,
        content="Test Content",
        author=author.profile,
    )
    yield fake_blog
    author.delete()


@pytest.fixture
def blog_with_blank_fields():
    author = User.objects.create(
        email="test323123@example.com",
        password="ewoacmoijsdoj@234",
        is_active=True,
        is_admin=True,
    )
    fake_blog = Blog.objects.create(
        title="",
        content="",
        author=author.profile,
    )
    yield fake_blog
    author.delete()


@pytest.fixture
def blog_response():
    validator = User.objects.create(
        email="test032408@test.com",
        password="testpassword!@#@#213",
        is_active=True,
        is_validator=True,
    )
    admin = User.objects.create(
        email="test092834@test.com",
        password="testpassword!@#@#2132",
        is_active=True,
        is_admin=True,
    )
    response = BlogResponse.objects.create(
        content="Test Response",
        response_to=admin.profile,
        author=validator.profile,
    )
    yield response
    if response.pk:
        response.delete()
        validator.delete()
        admin.delete()
