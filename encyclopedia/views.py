from django.shortcuts import render
from django.views.generic import ListView, DetailView
from encyclopedia.models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'encyclopedia/person-list.html'
    context_object_name = 'people'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'encyclopedia/person-dеtails.html'
    context_object_name = 'person'
    slug_url_kwarg = 'slug'

