from django.contrib import admin
from api.models import Device, Rate, Profile, DeviceRate

# Register your models here.
admin.site.register([Device, Rate, Profile, DeviceRate])
