from django.contrib import admin
from api.models import AccessTokenBlacklist
from django.contrib.auth import get_user_model

User= get_user_model()

# Register your models here.
admin.site.register(AccessTokenBlacklist)
admin.site.register(User)