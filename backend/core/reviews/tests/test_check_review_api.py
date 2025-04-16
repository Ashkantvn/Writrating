import pytest
from reviews.tests.fixtures import validator_client, device_review,admin_client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestCheckReviewApi:

    def test_PATCH_check_review_api_status_200(self,validator_client,device_review):
        client = validator_client
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "publishable": True,
        }
        response = client.patch(url,data=data)
        assert response.status_code == status.HTTP_200_OK
        device_review.refresh_from_db()
        assert device_review.publishable


    def test_PATCH_check_review_api_status_404(self,validator_client):
        client = validator_client
        url = reverse("reviews:check", args=["non-existent-slug"])
        data = {
            "publishable": True,
        }
        response = client.patch(url,data=data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        

    def test_PATCH_check_review_api_status_403(self,admin_client,device_review):
        client = admin_client
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "publishable": True,
        }
        response = client.patch(url,data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        device_review.refresh_from_db()
        assert not device_review.publishable

    def test_PATCH_check_review_api_status_401(self,device_review):
        client = APIClient()
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "publishable": True,
        }
        response = client.patch(url,data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        device_review.refresh_from_db()
        assert not device_review.publishable

    # POST method tests

    def test_POST_check_review_api_status_201(self,validator_client,device_review):
        client = validator_client
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "title": "Test title",
            "content": "Test content",
            "response_to": device_review.author
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_201_CREATED


    def test_POST_check_review_api_status_404(self,validator_client,device_review):
        client = validator_client
        url = reverse("reviews:check", args=["non-existent-slug"])
        data = {
            "title": "Test title",
            "content": "Test content",
            "response_to": device_review.author
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_404_NOT_FOUND


    def test_POST_check_review_api_status_403(self,admin_client,device_review):
        client = admin_client
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "title": "Test title",
            "content": "Test content",
            "response_to": device_review.author
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_POST_check_review_api_status_401(self,device_review):
        client = APIClient()
        url = reverse("reviews:check", args=[device_review.slug])
        data = {
            "title": "Test title",
            "content": "Test content",
            "response_to": device_review.author
        }
        response = client.post(url,data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED