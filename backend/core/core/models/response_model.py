from django.db import models
from accounts.models import Profile

class Response(models.Model):
    """
    Model to store the response of the checkings.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    response_to = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="target_responses",
    )

    
    class Meta:
        ordering = ['title']