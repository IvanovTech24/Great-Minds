from django.contrib import admin
from .models import Category, Work


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    exclude = ['slug']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'person', 'year_created', 'is_masterpiece']
    list_filter = ['is_masterpiece', 'categories']
    search_fields = ['title', 'person__last_name']
    exclude = ['slug']
