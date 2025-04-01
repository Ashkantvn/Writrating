from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
