from django.urls import reverse_lazy
from encyclopedia.models import Person
from encyclopedia.forms import PersonForm

class BasePersonView:
    model = Person
    form_class = PersonForm
    template_name = 'encyclopedia/person-form.html'
    success_url = reverse_lazy('encyclopedia:people')