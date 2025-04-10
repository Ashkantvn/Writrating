from core.models import Response


class DeviceResponse(Response):

    class Meta:
        proxy = True
        verbose_name = "Device Response"
    
    def __str__(self):
        return f"Device Response to {self.response_to} by {self.author.username}"