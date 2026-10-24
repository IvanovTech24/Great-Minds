from django.urls import reverse_lazy
from gallery.models import Work, Category
from gallery.forms import WorkForm, CategoryForm


class BaseWorkView:
    model = Work
    form_class = WorkForm
    template_name = 'gallery/work-form.html'
    success_url = reverse_lazy('gallery:works')


class BaseCategoryView:
    model = Category
    form_class = CategoryForm
    template_name = 'gallery/category-form.html'
    success_url = reverse_lazy('gallery:categories')