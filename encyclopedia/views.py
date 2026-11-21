from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from encyclopedia.models import Person, Era, Quote, Influence
from django.urls import reverse_lazy, reverse
from encyclopedia.mixins import BasePersonView, BaseEraView
from encyclopedia.forms import QuoteForm, InfluenceForm


class PersonListView(ListView):
    model = Person
    template_name = 'encyclopedia/person/person-list.html'
    context_object_name = 'people'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().select_related('era')

        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                models.Q(first_name__icontains=search_query) |
                models.Q(last_name__icontains=search_query)
            )

        era_name = self.request.GET.get('era')
        if era_name:
            queryset = queryset.filter(era__name=era_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eras'] = Era.objects.all()
        return context


class PersonDetailView(DetailView):
    model = Person
    template_name = 'encyclopedia/person/person-dеtails.html'
    context_object_name = 'person'
    slug_url_kwarg = 'slug'


class PersonCreateView(BasePersonView ,CreateView):
    ...


class PersonUpdateView(BasePersonView ,UpdateView):
    ...


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'encyclopedia/person/person-delete.html'
    success_url = reverse_lazy('encyclopedia:people')


class EraListView(ListView):
    model = Era
    template_name = 'encyclopedia/era/era-list.html'
    context_object_name = 'eras'


class EraDetailView(DetailView):
    model = Era
    template_name = 'encyclopedia/era/era-details.html'
    context_object_name = 'era'
    pk_url_kwarg = 'pk'


class EraCreateView(BaseEraView, CreateView):
    ...


class EraUpdateView(BaseEraView, UpdateView):
    ...


class EraDeleteView(DeleteView):
    model = Era
    template_name = 'encyclopedia/era/era-delete.html'
    success_url = reverse_lazy('encyclopedia:eras')


class QuoteCreateView(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'encyclopedia/quote/quote-form.html'

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save()
        return redirect('encyclopedia:detail', slug=self.object.person.slug)


class QuoteListView(ListView):
    model = Quote
    template_name = 'encyclopedia/quote/quote-list.html'
    context_object_name = 'quotes'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().select_related('person')


class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'encyclopedia/quote/quote-detail.html'
    context_object_name = 'quote'


class QuoteUpdateView(UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'encyclopedia/quote/quote-form.html'

    def get_success_url(self) -> str:
        return reverse(
            'encyclopedia:quote_detail',
            kwargs={
                'pk': self.object.pk
            }
        )


class QuoteDeleteView(DeleteView):
    model = Quote
    template_name = 'encyclopedia/quote/quote-delete.html'
    success_url = reverse_lazy('encyclopedia:quotes')



class InfluenceCreateView(CreateView):
    model = Influence
    form_class = InfluenceForm
    template_name = 'encyclopedia/influence/influence-form.html'
    success_url = reverse_lazy('encyclopedia:people')


class InfluenceListView(ListView):
    model = Influence
    template_name = 'encyclopedia/influence/influence-list.html'
    context_object_name = 'influences'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().select_related('influencer', 'influenced')


class InfluenceDetailView(DetailView):
    model = Influence
    template_name = 'encyclopedia/influence/influence-detail.html'
    context_object_name = 'influence'


class InfluenceUpdateView(UpdateView):
    model = Influence
    form_class = InfluenceForm
    template_name = 'encyclopedia/influence/influence-form.html'

    def get_success_url(self) -> str:
        return reverse(
            'encyclopedia:influence_detail',
            kwargs={
                'pk': self.object.pk
            }
        )


class InfluenceDeleteView(DeleteView):
    model = Influence
    template_name = 'encyclopedia/influence/influence-delete.html'
    success_url = reverse_lazy('encyclopedia:influences')