from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gallery.models import Work
from gallery.mixins import BaseWorkView

class WorkListView(ListView):
    model = Work
    template_name = 'gallery/work-list.html'
    context_object_name = 'works'


class WorkDetailView(DetailView):
    model = Work
    template_name = 'gallery/work-details.html'
    context_object_name = 'work'
    slug_url_kwarg = 'slug'


class WorkCreateView(BaseWorkView ,CreateView):
    ...

class WorkUpdateView(BaseWorkView ,UpdateView):
    ...

class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'gallery/work-delete.html'
    success_url = reverse_lazy('gallery:works')