import pytest
from fixtures import authenticated_client
from django.urls import reverse

@pytest.mark.django_db
class TestChangePassAPI:
    def test_POST_change_pass_user_status_200(self,authenticated_client):
        url = reverse("accounts:change")