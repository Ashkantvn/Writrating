from django.urls import path
from reviews.api.v1 import views

app_name = "reviews"

urlpatterns = [
    path("", views.ReviewsListAPIView.as_view(), name="list"),
    path("add/", views.ReviewAddAPIView.as_view(), name="add"),
    path("<str:slug>/", views.ReviewDetailsAPIView.as_view(), name="details"),
    path("<str:slug>/delete/", views.ReviewDeleteAPIView.as_view(), name="delete"),
    path("<str:slug>/edit/", views.ReviewEditAPIView.as_view(), name="edit"),
]