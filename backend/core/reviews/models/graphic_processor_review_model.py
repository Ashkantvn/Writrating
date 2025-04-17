from reviews.models import Review
from django.db import models
from devices import models as DevicesModel


class GraphicsProcessorReview(Review):
    target = models.ForeignKey(DevicesModel.GraphicProcessor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.target.graphic_processor_name} Review"
