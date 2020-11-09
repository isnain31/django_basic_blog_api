from django.contrib import admin

# Register your models here.
from .models import Blog, Category

admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Configure Tag panel"""
    list_display = ("title", "slug")