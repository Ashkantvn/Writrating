import pytest
from rest_framework import status
from django.urls import reverse
from reviews.tests.fixtures import device_review, admin_client, authenticated_client
from reviews import models
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAddReviewApi:
    def test_POST_add_review_status_201(self, admin_client, device_review):
        client = admin_client
        url = reverse("reviews:add")
        data = {
            "review_title": "device_review.review_title 123",
            "review_text": device_review.review_text,
            "rating": device_review.rating,
            "buying_worth": device_review.buying_worth,
            "published_date": device_review.published_date.strftime("%Y-%m-%d"),
            "target": device_review.target.slug,
            "target_type": "Device",
            "status": device_review.status,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert models.DeviceReview.objects.filter(
            review_title=data.get("review_title")
        ).exists()

    def test_POST_add_review_status_401(self, device_review):
        client = APIClient()
        url = reverse("reviews:add")
        data = {
            "review_title": "device_review.review_title 123",
            "review_text": device_review.review_text,
            "rating": device_review.rating,
            "buying_worth": device_review.buying_worth,
            "published_date": device_review.published_date.strftime("%Y-%m-%d"),
            "target": device_review.target.slug,
            "target_type": "Device",
            "status": device_review.status,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not models.DeviceReview.objects.filter(
            review_title=data.get("review_title")
        ).exists()

    def test_POST_add_review_status_403(self, authenticated_client, device_review):
        client = authenticated_client
        url = reverse("reviews:add")
        data = {
            "review_title": "device_review.review_title 123",
            "review_text": device_review.review_text,
            "rating": device_review.rating,
            "buying_worth": device_review.buying_worth,
            "published_date": device_review.published_date.strftime("%Y-%m-%d"),
            "target": device_review.target.slug,
            "target_type": "Device",
            "status": device_review.status,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert not models.DeviceReview.objects.filter(
            review_title=data.get("review_title")
        ).exists()

    def test_POST_add_review_status_400(self, admin_client):
        client = admin_client
        url = reverse("reviews:add")
        data = {
            "review_title": "Test Review Title",
            "review_text": "Test Review Text",
            "rating": 5,
            "buying_worth": "Test Buying Worth",
            "published_date": "2022-12-12",
            "status": False,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_POST_add_review_status_404(self, admin_client):
        client = admin_client
        url = reverse("reviews:add")
        data = {
            "review_title": "Test Review Title",
            "review_text": "Test Review Text",
            "rating": 5,
            "buying_worth": "Test Buying Worth",
            "published_date": "2022-12-12",
            "target": "test",
            "target_type": "Device",
            "status": False,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
