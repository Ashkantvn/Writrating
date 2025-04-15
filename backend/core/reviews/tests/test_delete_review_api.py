import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from reviews.tests.fixtures import device_review, authenticated_client, admin_client
from reviews import models
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestDeleteReviewApi:
    def test_DELETE_delete_review_status_204(self, admin_client, device_review):
        client = admin_client
        url = reverse("reviews:delete", args=[device_review.slug])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not models.DeviceReview.objects.filter(slug=device_review.slug).exists()

    def test_DELETE_delete_review_status_401(self, device_review):
        client = APIClient()
        url = reverse("reviews:delete", args=[device_review.slug])
        response = client.delete(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert models.DeviceReview.objects.filter(slug=device_review.slug).exists()

    def test_DELETE_delete_review_status_403(self, authenticated_client, device_review):
        client = authenticated_client
        url = reverse("reviews:delete", args=[device_review.slug])
        response = client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert models.DeviceReview.objects.filter(slug=device_review.slug).exists()

        # delete as other user
        client = APIClient()
        user = User.objects.create(
            email="4qZfO@example.com",
            password = "jasdnoifnav@#$%134234",
            is_admin=True,
            is_active=True
        )
        client.force_authenticate(user=user)
        url = reverse("reviews:delete", args=[device_review.slug])
        response = client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert models.DeviceReview.objects.filter(slug=device_review.slug).exists()

    
    