from django.contrib import admin
from blogs.models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_date']
    search_fields = ['title', 'author']
    list_filter = ['create_date']
    date_hierarchy = 'published_date'
    ordering = ['create_date']
    readonly_fields = ['create_date', 'update_date']