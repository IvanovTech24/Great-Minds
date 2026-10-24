from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from encyclopedia.models import Person, Era, Quote, Influence
from django.urls import reverse_lazy
from encyclopedia.mixins import BasePersonView, BaseEraView
from encyclopedia.forms import QuoteForm, InfluenceForm

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


class EraListView(ListView):
    model = Era
    template_name = 'encyclopedia/era-list.html'
    context_object_name = 'eras'


class EraDetailView(DetailView):
    model = Era
    template_name = 'encyclopedia/era-details.html'
    context_object_name = 'era'
    pk_url_kwarg = 'pk'


class EraCreateView(BaseEraView, CreateView):
    ...


class EraUpdateView(BaseEraView, UpdateView):
    ...


class EraDeleteView(DeleteView):
    model = Era
    template_name = 'encyclopedia/era-delete.html'
    success_url = reverse_lazy('encyclopedia:eras')


class QuoteCreateView(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'encyclopedia/quote-form.html'

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save()
        return redirect('encyclopedia:detail', slug=self.object.person.slug)



class InfluenceCreateView(CreateView):
    model = Influence
    form_class = InfluenceForm
    template_name = 'encyclopedia/influence-form.html'
    success_url = reverse_lazy('encyclopedia:people')