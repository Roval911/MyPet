from django.contrib import admin
from .models import Post




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Автоматически заполняет поле slug при через админку"""
    prepopulated_fields = {'slug': ('title',)}