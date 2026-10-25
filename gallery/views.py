from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gallery.models import Work, Category
from gallery.mixins import BaseWorkView, BaseCategoryView
from gallery.forms import CategoryForm

class WorkListView(ListView):
    model = Work
    template_name = 'gallery/work/work-list.html'
    context_object_name = 'works'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().select_related('person').prefetch_related('categories')

        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        category_name = self.request.GET.get('category')
        if category_name:
            queryset = queryset.filter(categories__name=category_name)

        masterpiece_filter = self.request.GET.get('masterpiece')
        if masterpiece_filter == 'yes':
            queryset = queryset.filter(is_masterpiece=True)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class WorkDetailView(DetailView):
    model = Work
    template_name = 'gallery/work/work-details.html'
    context_object_name = 'work'
    slug_url_kwarg = 'slug'


class WorkCreateView(BaseWorkView ,CreateView):
    ...

class WorkUpdateView(BaseWorkView ,UpdateView):
    ...

class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'gallery/work/work-delete.html'
    success_url = reverse_lazy('gallery:works')


class CategoryListView(ListView):
    model = Category
    template_name = 'gallery/category/category-list.html'
    context_object_name = 'categories'


class CategoryCreateView(BaseCategoryView, CreateView):
    ...


class CategoryUpdateView(BaseCategoryView, UpdateView):
    ...


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'gallery/category/category-delete.html'
    success_url = reverse_lazy('gallery:categories')