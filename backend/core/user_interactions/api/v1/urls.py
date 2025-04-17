from django.urls import path
from user_interactions.api.v1 import views

app_name = "interactions"

urlpatterns = [
    path("compare/<str:slug1>/<str:slug2>/", views.CompareDevicesAPIView.as_view(), name="compare-devices"),
    path("report/",views.ReportingSystemAPIView.as_view(), name="report"),
]
