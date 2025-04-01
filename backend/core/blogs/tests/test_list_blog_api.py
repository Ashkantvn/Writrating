import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestBlogListAPI:

    def test_GET_blog_list_status_200(self):
        client = APIClient()
        url = reverse("blogs:list")
        response = client.get(url)
        assert response.status_code == 200
