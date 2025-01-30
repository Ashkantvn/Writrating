from django.contrib import admin
from blogs.models import Blog

# Actions for the admin panel
def make_publishable(modeladmin, request, queryset):
    queryset.update(publishable=True)

make_publishable.short_description = "Mark selected blogs as publishable"

def make_unpublishable(modeladmin, request, queryset):
    queryset.update(publishable=False)

make_unpublishable.short_description = "Mark selected blogs as unpublishable"

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_date']
    search_fields = ['title', 'author']
    list_filter = ['create_date','published_date','publishable']
    date_hierarchy = 'published_date'
    ordering = ['create_date']
    readonly_fields = ['create_date', 'update_date','views','slug']
    fieldsets = (
        ('Blog Information', {
            'fields': (
                'title', 
                'banner', 
                'content', 
                'status', 
                'publishable', 
                'author', 
                'tags', 
                'categories', 
                'published_date',
                )
        }),
    )
    actions = [make_publishable, make_unpublishable]