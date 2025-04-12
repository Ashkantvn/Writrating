from django.db import models


# Device images
class DeviceImages(models.Model):
    device = models.ForeignKey(
        'Device', on_delete=models.CASCADE, related_name='device_images', blank=False
    )
    device_image = models.ImageField(upload_to='device_images/', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.device.device_name}"

# Device features
class DeviceFeatures(models.Model):
    accessories = models.CharField(max_length=255, blank=False)
    security = models.CharField(max_length=255, blank=False)
    warranty_and_support = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device.device_name} Features"

# Device software information
class DeviceSoftwareInformation(models.Model):
    ui = models.CharField(max_length=255, blank=False)
    os = models.ForeignKey(
        'OperatingSystem', on_delete=models.SET_NULL,null=True, related_name='device_software_info', blank=False
    )
    pre_installed_softwares = models.CharField(max_length=255, blank=False)
    update_policy = models.CharField(max_length=255,blank=False)
    customizability = models.CharField(max_length=255,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.device.device_name} Software Information"

# Device hardware information
class DeviceHardwareInformation(models.Model):
    battery = models.CharField(max_length=255, blank=False)
    memory = models.IntegerField(blank=False)
    storage = models.CharField(max_length=255, blank=False)
    sensors = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    processor = models.ForeignKey(
        'Processor', on_delete=models.SET_NULL,null=True, related_name='device_hardware_info', blank=False
    )
    graphic_processor = models.ForeignKey(
        'GraphicProcessor', on_delete=models.SET_NULL,null=True, related_name='device_hardware_info', blank=False
    )
    display = models.ForeignKey(
        'Display', on_delete=models.SET_NULL,null=True, related_name='device_hardware_info', blank=False
    )
    camera = models.ForeignKey(
        'Camera', on_delete=models.SET_NULL,null=True, related_name='device_hardware_info', blank=False
    )

    
    def __str__(self):
        return f"{self.device.device_name} Hardware Information"

# Device physical information
class DevicePhysicalInformation(models.Model):
    width = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    thickness = models.FloatField(blank=False)
    wireless_connectivity = models.CharField(max_length=255, blank=False)
    ports = models.CharField(max_length=255, blank=False)
    material = models.CharField(max_length=255, blank=False)
    device_color = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device.device_name} Physical Information"

# Device category
class DeviceCategory(models.Model):
    category_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
