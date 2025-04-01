import pytest
from blogs.tests.fixtures import authenticated_admin_client, authenticated_user_client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blogs.models.blogs_model import Blog


@pytest.mark.django_db
class TestBlogAddAPI:

    def test_POST_blog_add_status_201(self, authenticated_admin_client):
        client = authenticated_admin_client
        url = reverse("blogs:add")
        response = client.post(
            url,
            {
                "title": "Test Blog",
                "content": "Test Content",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Blog.objects.filter(title="Test Blog").exists()

    def test_POST_blog_add_status_401(self):
        client = APIClient()
        url = reverse("blogs:add")
        response = client.post(url, {"title": "Test Blog", "content": "Test content"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not Blog.objects.filter(title="Test Blog").exists()

    def test_POST_blog_add_status_400(self, authenticated_admin_client):
        client = authenticated_admin_client
        url = reverse("blogs:add")
        response = client.post(
            url,
            {
                "title": "Test Blog" * 60,
                "content": "Test Content",
            },
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Test for duplicated blog
        client.post(
            url,
            {
                "title": "Test Blog",
                "content": "Test Content",
            },
        )
        response = client.post(
            url,
            {
                "title": "Test Blog",
                "content": "Another Content",
            },
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Test for missing fields
        client.post(
            url,
            {
                "title": "",
                "content": "Test Content",
            },
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response = client.post(
            url,
            {
                "title": "Test Blog2",
                "content": "",
            },
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not Blog.objects.filter(title="Test Blog2").exists()

    def test_POST_blog_add_status_403(self, authenticated_user_client):
        client = authenticated_user_client
        url = reverse("blogs:add")
        response = client.post(
            url,
            {
                "title": "Test Blog",
                "content": "Test Content",
            },
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert not Blog.objects.filter(title="Test Blog").exists()
