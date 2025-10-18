from django.db import models
from django.utils.text import slugify


class Device(models.Model):
    device_name = models.CharField(max_length=100, unique=True, db_index=True)
    rates = models.ManyToManyField("Rate", through="DeviceRate")
    device_slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        if (
            not self.device_slug or self.device_slug !=
            slugify(self.device_name)
        ):
            self.device_slug = slugify(self.device_name)
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
