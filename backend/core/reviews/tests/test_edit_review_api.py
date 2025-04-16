import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from reviews.tests.fixtures import device_review  ,authenticated_client, admin_client
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestEditReviewAPI:

    def test_PATCH_edit_review_status_200(self, device_review):
        client = APIClient()
        url = reverse("reviews:edit", args=[device_review.slug])
        user = User.objects.get(profile=device_review.author)
        # Simulate authentication
        client.force_authenticate(user=user)
        data = {
            "review_text": "Updated review content.",
            "rating": 4,
        }
        response = client.patch(url, data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        device_review.refresh_from_db()
        assert device_review.review_text == data["review_text"]
        

    def test_PATCH_edit_review_status_401(self, device_review):
        client = APIClient()
        url = reverse("reviews:edit", args=[device_review.slug])
        data = {
            "review_text": "Updated review content.",
            "rating": 4,
        }
        response = client.patch(url, data=data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_PATCH_edit_review_status_403(self, authenticated_client, device_review):
        client = authenticated_client
        url = reverse("reviews:edit", args=[device_review.slug])
        data = {
            "review_text": "Updated review content.",
            "rating": 4,
        }
        response = client.patch(url, data=data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        device_review.refresh_from_db()
        assert device_review.review_text != data["review_text"]


    def test_PATCH_edit_review_status_403_admin(self, device_review):
        client = APIClient()
        user = User.objects.create(
            email = "soiu234@test.com",
            password = "opqiewmu@!232358",
            is_admin = True,
            is_active = True,
        )
        client.force_authenticate(user=user)
        url = reverse("reviews:edit", args=[device_review.slug])
        data = {
            "review_text": "Updated review content.",
            "rating": 4,
        }
        response = client.patch(url, data=data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        device_review.refresh_from_db()
        assert device_review.review_text != data["review_text"]

    def test_PATCH_edit_review_status_404(self, admin_client):
        client = admin_client
        url = reverse("reviews:edit", args=["non-existent-slug"])
        data = {
            "review_text": "Updated review content.",
            "rating": 4,
        }
        response = client.patch(url, data=data, format='json')
        assert response.status_code == status.HTTP_404_NOT_FOUND