from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=100)
    rates = models.ManyToManyField('Rate', through='DeviceRate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name