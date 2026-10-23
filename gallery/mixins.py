from django.urls import reverse_lazy
from gallery.models import Work
from gallery.forms import WorkForm

class BaseWorkView:
    model = Work
    form_class = WorkForm
    template_name = 'gallery/work-form.html'
    success_url = reverse_lazy('gallery:works')