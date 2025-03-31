from core.models import Response
from accounts.models import Profile
from django.db import models

class BlogResponse(Response):
    """
    BlogResponse model that inherits from Response.
    This model is used to store responses related to blog posts.
    """
    response_to = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='blog_responses',
    )

    class Meta:
        verbose_name = 'Blog Response'

    def __str__(self):
        return f'Blog Response to {self.response_to} by {self.author.username}'