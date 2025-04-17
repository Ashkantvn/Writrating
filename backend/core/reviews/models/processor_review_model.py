from reviews.models import Review
from django.db import models
from devices import models as DevicesModel


class ProcessorReview(Review):
    target = models.ForeignKey(DevicesModel.Processor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.target.processor_name} Review"
