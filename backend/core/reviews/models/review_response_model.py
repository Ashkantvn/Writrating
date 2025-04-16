from core.models import Response
from django.db import models

class ReviewResponse(Response):

    class Meta:
        proxy = True

    def __str__(self):
        return f"Review Response to {self.response_to} by {self.author.username}"
    