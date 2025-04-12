from django.urls import path
from devices.api.v1 import views

app_name = "devices"

urlpatterns = [
    path('',views.DevicesListAPIView.as_view(), name='list'),
    path('add/',views.DevicesAddAPIView.as_view(), name='add'),
    path('<str:slug>/',views.DeviceDetailsAPIView.as_view(), name='details'),
    path('<str:slug>/edit/',views.DeviceEditAPIView.as_view(), name='edit'),
    path('<str:slug>/delete/',views.DeviceDeleteAPIView.as_view(), name='delete'),
    # path('<str:slug>/check/',views.DevicesCheckAPIView.as_view(), name='check'),
]
