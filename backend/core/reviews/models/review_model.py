from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Review(models.Model):
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    status = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    buying_worth = models.CharField(max_length=255)
    review_text = models.TextField()
    publishable = models.BooleanField(default=False)
    review_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    published_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    created_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True
        app_label = "reviews"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.review_title)
        return super().save(*args, **kwargs)
