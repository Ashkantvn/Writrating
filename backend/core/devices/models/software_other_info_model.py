from django.db import models
from django.utils.text import slugify


class OperatingSystem(models.Model):
    os_name = models.CharField(max_length=255, blank=False)
    kernel = models.CharField(max_length=255, blank=False)
    os_version = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    publishable = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.os_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.os_name)
        return super().save(*args, **kwargs)
