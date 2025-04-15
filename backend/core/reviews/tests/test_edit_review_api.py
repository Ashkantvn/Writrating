import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from reviews.tests.fixtures import device_review   

@pytest.mark.django_db
class TestEditReviewAPI:

    def test_PATCH_edit_review_status_200(self, admin_client, device_review):
        pass

    def test_PATCH_edit_review_status_401(self, device_review):
        pass

    def test_PATCH_edit_review_status_403(self, authenticated_client, device_review):
        pass

    def test_PATCH_edit_review_status_400(self, admin_client):
        pass