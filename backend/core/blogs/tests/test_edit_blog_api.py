import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from blogs.tests.fixtures import authenticated_admin_client,blog,Blog

@pytest.mark.django_db
class TestEditBlogAPI:
    
    def test_edit_blog_status_code_401(self):
        """
        Test that the edit blog API returns a 401 status code when the user is not authenticated.
        """
        client = APIClient()
        url = reverse('blogs:edit', kwargs={'slug':'test-blog'})
        response = client.patch(url, data={
            'title': 'New Title',
            'content': 'New Content'
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_edit_blog_status_code_403(self,authenticated_admin_client,blog):
        """
        Test that the edit blog API returns a 403 status code when the user wants to edit a blog that does not belong to them.
        """
        client = authenticated_admin_client
        url = reverse('blogs:edit', kwargs={'slug':blog.slug})
        response = client.patch(url, data={
            'title': 'New Title',
            'content': 'New Content'
        })
        assert response.status_code == status.HTTP_403_FORBIDDEN
        blog.refresh_from_db()
        assert blog.title == 'Test Blog'
        
    def test_edit_blog_status_code_404(self,authenticated_admin_client):
        """
        Test that the edit blog API returns a 404 status code when the blog does not exist.
        """
        client = authenticated_admin_client
        url = reverse('blogs:edit', kwargs={'slug':'non-existent-blog'})
        response = client.patch(url, data={
            'title': 'New Title',
            'content': 'New Content'
        })
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_edit_blog_status_code_200(self,blog):
        """
        Test that the edit blog API returns a 200 status code when the blog is successfully edited.
        """
        client= APIClient()
        client.force_authenticate(user=blog.author.user)
        url = reverse('blogs:edit', kwargs={'slug':blog.slug})
        response = client.patch(url, data={
            'title': 'New Title',
            'content': 'New Content'
        })
        assert response.status_code == status.HTTP_200_OK
        blog.refresh_from_db()
        assert blog.title == 'New Title'
        assert blog.content == 'New Content'


        