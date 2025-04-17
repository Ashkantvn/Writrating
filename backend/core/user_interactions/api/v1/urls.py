from django.urls import path
from user_interactions.api.v1.views import CompareDevicesAPIView

app_name = "interactions"

urlpatterns = [
    path("compare/<str:slug1>/<str:slug2>/", CompareDevicesAPIView.as_view(), name="compare-devices"),
]
