from django.db import models 
from django.utils.text import slugify

class Device(models.Model):
    """
    Represents a device in the system.
    """

    device_name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(default=0.0)
    release_date = models.DateField(blank=False)
    physical_information = models.OneToOneField(
        'DevicePhysicalInformation', on_delete=models.CASCADE, related_name='device',blank=False
    )
    hardware_information = models.OneToOneField(
        'DeviceHardwareInformation', on_delete=models.CASCADE, related_name='device',blank=False
    )
    software_information = models.OneToOneField(
        'DeviceSoftwareInformation', on_delete=models.CASCADE, related_name='device',blank=False
    )
    category = models.ForeignKey(
        'DeviceCategory', on_delete=models.CASCADE, related_name='devices',blank=False
    )
    features = models.OneToOneField(
        'DeviceFeatures', on_delete=models.CASCADE, related_name='devices',blank=False
    )
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.device_name)
        return super().save(*args, **kwargs)