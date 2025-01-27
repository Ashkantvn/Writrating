import pytest
from blogs.models.blogs_model import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def blog():
        return Blog.objects.create(
            title='Test Blog', 
            content='Test Content',
            author=User,
            )