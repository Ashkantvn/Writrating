from django.db import models

class DeviceRate(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    rate = models.ForeignKey('Rate', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('device', 'rate')

    def __str__(self):
        return f"{self.device} - {self.rate}"
