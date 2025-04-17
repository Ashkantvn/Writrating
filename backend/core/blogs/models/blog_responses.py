from core.models import Response


class BlogResponse(Response):
    """
    BlogResponse model that inherits from Response.
    This model is used to store responses related to blog posts.
    """

    class Meta:
        proxy = True
        verbose_name = "Blog Response"

    def __str__(self):
        return f"Blog Response to {self.response_to} by {self.author.username}"
