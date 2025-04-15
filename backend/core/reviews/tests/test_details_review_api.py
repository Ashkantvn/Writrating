import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from reviews.tests.fixtures import device_review

@pytest.mark.django_db
class TestDetailsReviewAPI:
    def test_GET_review_status_200(self, device_review):
        client = APIClient()
        url = reverse("reviews:details", args=[device_review.slug])
        reponse = client.get(url)
        assert reponse.status_code == status.HTTP_200_OK
        

    def test_GET_review_status_404(self):
        client = APIClient()
        url = reverse("reviews:details", args=["non-existent-slug"])
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND