from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


# Processor
class Processor(models.Model):
    processor_name = models.CharField(max_length=255, blank=False)
    core = models.CharField(max_length=255, blank=False)
    refresh_rate = models.CharField(max_length=255, blank=False)
    cache = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    processor_technology = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(unique=True)
    publishable = models.BooleanField(default=False)
    release_date = models.DateField(default=now, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.processor_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.processor_name)
        return super().save(*args, **kwargs)


# Graphic processor
class GraphicProcessor(models.Model):
    graphic_processor_name = models.CharField(max_length=255, blank=False)
    g_ram = models.IntegerField(blank=False)
    ram_type = models.CharField(max_length=255, blank=False)
    publishable = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    release_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.graphic_processor_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.graphic_processor_name)
        return super().save(*args, **kwargs)


# Camera
class Camera(models.Model):
    description = models.TextField(blank=False)
    resolution = models.CharField(max_length=255, blank=False)
    features = models.CharField(max_length=255, blank=False)
    zoom = models.IntegerField(blank=False)
    software_features = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description}"


# Display
class Display(models.Model):
    size = models.CharField(max_length=255, blank=False)
    resolution = models.CharField(max_length=255, blank=False)
    protection = models.CharField(max_length=255, blank=False)
    technology = models.CharField(max_length=255, blank=False)
    refresh_rate = models.IntegerField(blank=False)
    brightness = models.IntegerField(blank=False)
    features = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.size} Display ({self.pk})"
