from django.contrib import admin
from reviews import models

# Register your models here.
admin.site.register(
    [
        models.DeviceReview,
        models.OperatingSystemReview,
        models.ProcessorReview,
        models.GraphicsProcessorReview,
    ]
)
