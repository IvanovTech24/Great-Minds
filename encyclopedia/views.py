from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from encyclopedia.models import Person
from django.urls import reverse_lazy
from encyclopedia.mixins import BasePersonView

class PersonListView(ListView):
    model = Person
    template_name = 'encyclopedia/person-list.html'
    context_object_name = 'people'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'encyclopedia/person-dеtails.html'
    context_object_name = 'person'
    slug_url_kwarg = 'slug'


class PersonCreateView(BasePersonView ,CreateView):
    ...


class PersonUpdateView(BasePersonView ,UpdateView):
    ...


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'encyclopedia/person-delete.html'
    success_url = reverse_lazy('encyclopedia:people')