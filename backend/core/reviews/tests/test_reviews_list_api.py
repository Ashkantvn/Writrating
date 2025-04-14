import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestReviewsListApi:

    def test_GET_reviews_list_status_200(self):
        client = APIClient()
        url = reverse("reviews:list")
        respnose = client.get(url)
        assert respnose.status_code == 200
