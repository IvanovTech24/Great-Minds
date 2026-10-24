from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gallery.models import Work, Category
from gallery.mixins import BaseWorkView, BaseCategoryView
from gallery.forms import CategoryForm

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


class CategoryListView(ListView):
    model = Category
    template_name = 'gallery/category-list.html'
    context_object_name = 'categories'


class CategoryCreateView(BaseCategoryView, CreateView):
    ...


class CategoryUpdateView(BaseCategoryView, UpdateView):
    ...


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'gallery/category-delete.html'
    success_url = reverse_lazy('gallery:categories')