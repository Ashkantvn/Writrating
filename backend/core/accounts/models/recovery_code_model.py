from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class RecoveryCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    digits = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.digits}"
