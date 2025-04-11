from django.contrib import admin
from devices import models

# Register your models here.
admin.site.register(models.Device)
admin.site.register(models.Camera)
admin.site.register(models.Display)
admin.site.register(models.Processor)
admin.site.register(models.GraphicProcessor)
admin.site.register(models.DeviceCategory)
admin.site.register(models.DeviceFeatures)
admin.site.register(models.DeviceImages)
admin.site.register(models.DevicePhysicalInformation)
admin.site.register(models.DeviceSoftwareInformation)
admin.site.register(models.DeviceHardwareInformation)
admin.site.register(models.OperatingSystem)
admin.site.register(models.DeviceResponse)