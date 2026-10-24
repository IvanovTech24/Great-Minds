from django.urls import reverse_lazy
from encyclopedia.models import Person, Era
from encyclopedia.forms import PersonForm, EraForm

class BasePersonView:
    model = Person
    form_class = PersonForm
    template_name = 'encyclopedia/person-form.html'
    success_url = reverse_lazy('encyclopedia:people')


class BaseEraView:
    model = Era
    form_class = EraForm
    template_name = 'encyclopedia/era-form.html'
    success_url = reverse_lazy('encyclopedia:eras')