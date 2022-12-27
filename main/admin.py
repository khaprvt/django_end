from django.contrib import admin
from .models import PostModel

# Register your models here.

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_display_links = ['id', 'name']
    list_filter = ['created_at']