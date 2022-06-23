from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'published', 'price']
    search_fields = ['title', 'description']
