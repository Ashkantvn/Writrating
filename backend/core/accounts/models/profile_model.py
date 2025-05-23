from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Profile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    profile_image = models.ImageField(
        upload_to="images/profiles", default="images/profiles/Default.jpg", blank=True
    )
    description = models.TextField(blank=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.username:
            return f"{self.username}'s profile"
        return f"{self.pk}"

    def clean(self):
        invalid_chars = set("!@#$%^&*()+=[]{}|\\:;\"'<>,.?/")
        if " " in self.username:
            raise ValidationError("Username should not contain spaces")
        if any(char in invalid_chars for char in self.username):
            raise ValidationError("Username contains invalid characters")

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.username = f"user{self.pk}"
            super().save(update_fields=["username"])
        else:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise Exception(
            "Profile cannot be deleted directly. Delete the associated user instead."
        )
