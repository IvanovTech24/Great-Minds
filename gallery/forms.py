from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from gallery.models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ['slug']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Mona Lisa'
                }
            ),
            'year_created': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. 1503'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. ...'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                }
            ),
            'is_masterpiece': forms.CheckboxInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                }
            ),
        }

    def clean_year_created(self):
        year_created = self.cleaned_data.get('year_created')
        current_year = timezone.now().year

        if year_created and year_created > current_year:
                raise ValidationError("The creation year cannot be in the future.")

        return year_created