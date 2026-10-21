from django.contrib import admin
from .models import Era, Person, Quote, Influence


@admin.register(Era)
class EraAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_year', 'end_year']
    search_fields = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_year', 'era']
    list_filter = ['era']
    search_fields = ['first_name', 'last_name']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'person']
    search_fields = ['text']


@admin.register(Influence)
class InfluenceAdmin(admin.ModelAdmin):
    list_display = ['influencer', 'influenced']
    search_fields = ['influencer__last_name', 'influenced__last_name']

