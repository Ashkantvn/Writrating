import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blogs.tests.fixtures import authenticated_validator_client,blog, authenticated_user_client



@pytest.mark.django_db
class TestCheckBlogAPI:
    
    # GET request tests
    def test_GET_check_blog_api_status_200(self, authenticated_validator_client, blog):
        """
        Test the GET request to get the blog API returns a 200 status code
        and the expected response data.
        """
        url = reverse('blogs:check', args=[blog.slug])
        response = authenticated_validator_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == blog.title

    def test_GET_check_blog_api_status_404(self, authenticated_validator_client):
        """
        Test GET request return 404 status code when blog does not exist
        """
        url = reverse('blogs:check', kwargs={'slug':'non-existent-slug'})
        response = authenticated_validator_client.get(url)
        
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_GET_check_blog_api_status_401(self):
        """
        Test GET request to get the blog API returns a 401 status code
        when the user is not authenticated.
        """
        url = reverse('blogs:check', kwargs={'slug':'non-existent-slug'})
        client = APIClient()
        response = client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_GET_check_blog_api_status_403(self,authenticated_user_client):
        """
        Test GET request to get blog API returns a 403 status code
        when the user does not have permission to access the blog.
        """
        url = reverse('blogs:check',kwargs={'slug':'test-blog'})
        client = authenticated_user_client
        response = client.get(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    
    # POST request tests
    def test_POST_check_blog_api_status_200(self, authenticated_validator_client):
        """
        Test POST request to send response of checking blog returns a 200 status code
        """
        pass

    def test_POST_check_blog_api_status_404(self, authenticated_validator_client):
        pass

    def test_POST_check_blog_api_status_401(self, authenticated_validator_client):
        pass

    def test_POST_check_blog_api_status_403(self, authenticated_validator_client):
        pass
    
    # PATCH request tests
    def test_PATCH_check_blog_api_status_200(self, authenticated_validator_client):
        pass

    def test_PATCH_check_blog_api_status_404(self, authenticated_validator_client):
        pass

    def test_PATCH_check_blog_api_status_401(self, authenticated_validator_client):
        pass

    def test_PATCH_check_blog_api_status_403(self, authenticated_validator_client):
        pass

    # slug test
    def test_check_blog_api_invalid_slug(self, authenticated_validator_client):
        pass


