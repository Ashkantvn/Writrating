import pytest
from django.urls import reverse
from blogs.tests.fixtures import blog
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestRetrieveBlogApi:

    def test_GET_retrieve_blog_status_200(self,blog):
        client = APIClient()
        url = reverse('blogs:details',kwargs={'slug':blog.slug})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == blog.title
        assert response.data['content'] == blog.content
        

    def test_GET_retrieve_blog_status_404(self):
        client = APIClient()
        url = reverse('blogs:details',kwargs={'slug':'something-else'})
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_GET_retrieve_blog_status_400(self):
        client = APIClient()
        url = reverse('blogs:details',kwargs={'slug':'invalid@slug!example'})
        response = client.get(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
