from reviews.models import Review
from django.db import models
from devices import models as DevicesModel

class DeviceReview(Review):
    target = models.ForeignKey(DevicesModel.Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.target.device_name} Review"