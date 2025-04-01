import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from blogs.tests.fixtures import (
    authenticated_admin_client,
    blog,
    authenticated_user_client,
)
from blogs.models import Blog


@pytest.mark.django_db
class TestDeleteBlogAPI:

    def test_DELETE_blog_delete_api_status_401(self):
        """ "
        Test that the API returns 401 Unauthorized when no authentication is provided."
        """
        client = APIClient()
        url = reverse("blogs:delete", kwargs={"slug": "test-blog"})
        response = client.delete(url)
        assert response.status_code == 401

    def test_DELETE_blog_delete_api_status_404(self, authenticated_admin_client):
        """
        Test that the API returns 404 Not Found when the blog does not exist.
        """
        client = authenticated_admin_client
        url = reverse("blogs:delete", kwargs={"slug": "test-blog"})
        response = client.delete(url)
        assert response.status_code == 404

    def test_DELETE_blog_delete_api_status_403(self, authenticated_admin_client, blog):
        """
        Test that the API returns 403 Forbidden,
        and the blog still exists when a user attempts to delete a blog they do not own.
        """
        client = authenticated_admin_client
        url = reverse("blogs:delete", kwargs={"slug": blog.slug})
        response = client.delete(url)
        assert response.status_code == 403
        assert Blog.objects.filter(slug=blog.slug).exists()

    def test_DELETE_blog_delete_api_status_403_for_normal_user(
        self, authenticated_user_client
    ):
        """
        Test that the API returns 403 Forbidden when a normal user try to delete a blog.
        """
        client = authenticated_user_client
        url = reverse("blogs:delete", kwargs={"slug": "test-blog"})
        response = client.delete(url)
        assert response.status_code == 403

    def test_DELETE_blog_delete_api_status_400(self, authenticated_admin_client):
        """
        Test that the API returns 400 Bad Request when the slug is invalid.
        """
        client = authenticated_admin_client
        url = reverse("blogs:delete", kwargs={"slug": "my@invalid#slug!"})
        response = client.delete(url)
        assert response.status_code == 400

    def test_DELETE_blog_delete_api_status_200(self, blog):
        """
        Test that the API returns 200 OK, and blog successfully deleted.
        """
        client = APIClient()
        client.force_authenticate(user=blog.author.user)
        url = reverse("blogs:delete", kwargs={"slug": blog.slug})
        response = client.delete(url)
        assert response.status_code == 200
        assert not Blog.objects.filter(slug="test-blog").exists()
