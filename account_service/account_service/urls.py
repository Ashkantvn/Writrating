from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/admin/', admin.site.urls),
    # API url
    path("api/", include("api.urls"))
]
