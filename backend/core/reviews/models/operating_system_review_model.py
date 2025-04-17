from reviews.models import Review
from django.db import models
from devices import models as DevicesModel


class OperatingSystemReview(Review):
    target = models.ForeignKey(DevicesModel.OperatingSystem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.target.os_name} Review"
