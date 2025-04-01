from django.urls import path
from blogs.api.v1 import views


app_name = "blogs"

urlpatterns = [
    path("list/", views.BlogListAPIView.as_view(), name="list"),
    path("add/", views.BlogAddAPIView.as_view(), name="add"),
    path("<str:slug>/", views.BlogRetrieveAPIView.as_view(), name="details"),
    path("<str:slug>/edit/", views.BlogEditAPIView.as_view(), name="edit"),
    path("<str:slug>/delete/", views.BlogDeleteAPIView.as_view(), name="delete"),
    path("<str:slug>/check/", views.BlogCheckAPIView.as_view(), name="check"),
]
