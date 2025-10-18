from django.urls import path
from api.v1 import views

app_name = "v1"

urlpatterns = [
    path("devices/", views.DeviceListView.as_view(), name="list"),
    path(
        "devices/<slug:device_slug>/",
        views.DeviceRetrieveView.as_view(),
        name="retrieve",
    ),
]
