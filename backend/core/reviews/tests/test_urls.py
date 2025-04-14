import pytest
from django.urls import reverse , resolve
from reviews.api.v1 import views


@pytest.mark.django_db
class TestReviewUrls:

    def test_reviews_list_is_resolved(self):
        url = reverse("reviews:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.ReviewsListAPIView