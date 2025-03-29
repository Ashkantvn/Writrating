import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

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