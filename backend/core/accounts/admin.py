from django.contrib import admin
from accounts.models import CustomUser, Profile
from accounts.forms import CustomUserCreationForm

# Admin actions for users
def change_is_activate_to_false(modeladmin, request, queryset):
    queryset.update(status=False)
    change_is_activate_to_false.short_description = "Change activate to false"

def change_is_validator_to_false(modeladmin, request, queryset):
    queryset.update(status=False)
    change_is_validator_to_false.short_description = "Change validator to false"

def change_is_admin_to_false(modeladmin, request, queryset):
    queryset.update(status=False)
    change_is_admin_to_false.short_description = "Change admin to false"

def change_is_activate_to_true(modeladmin, request, queryset):
    queryset.update(status=True)
    change_is_activate_to_true.short_description = "Change activate to True"

def change_is_validator_to_true(modeladmin, request, queryset):
    queryset.update(status=True)
    change_is_validator_to_true.short_description = "Change validator to True"

def change_is_admin_to_true(modeladmin, request, queryset):
    queryset.update(status=True)
    change_is_admin_to_true.short_description = "Change admin to True"


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email',"is_admin","is_validator","is_active","is_superuser","last_login","updated_date","created_date",)
    list_filter = ('email',"is_admin","is_validator","is_active","is_superuser","last_login","created_date")

    fieldsets = ( 
        ("General information", {'fields': ('email', 'password1', 'password2')}),
        ("Roles and Permissions", {'fields': ('groups',)}),
        )

    search_fields = ("email",)
    ordering = ("email",)

    actions= (
        change_is_activate_to_false,
        change_is_activate_to_true,
        change_is_admin_to_false,
        change_is_admin_to_true,
        change_is_validator_to_false,
        change_is_validator_to_true,
        )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

    def has_delete_permission(self, request, obj = ...):
        return False
