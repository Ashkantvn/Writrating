from django.urls import path
from reviews.api.v1 import views

app_name = "reviews"

urlpatterns = [
    path("", views.ReviewsListAPIView.as_view(), name="list"),
]