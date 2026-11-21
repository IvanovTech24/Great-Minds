from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from gallery.models import Work, Category

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ['slug', 'created_by']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Mona Lisa'
                }
            ),
            'person': forms.Select(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                }
            ),
            'categories': forms.SelectMultiple(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500 h-32'
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
                    'class': 'h-6 w-6 text-amber-500 bg-gray-700 border-gray-600 rounded focus:ring-amber-500 mt-2',
                }
            ),
        }

    def clean_year_created(self):
        year_created = self.cleaned_data.get('year_created')
        current_year = timezone.now().year

        if year_created and year_created > current_year:
                raise ValidationError("The creation year cannot be in the future.")

        return year_created

    def clean(self):
        cleaned_data = super().clean()
        person = cleaned_data.get('person')
        year_created = cleaned_data.get('year_created')

        if person and year_created:
            if person.birth_year and year_created < person.birth_year:
                self.add_error(
                    'year_created',
                    f"This work cannot be created before its author was born "
                    f"({person.birth_year})."
                )
            if person.death_year and year_created > person.death_year:
                self.add_error(
                    'year_created',
                    f"This work cannot be created after its author's death "
                    f"({person.death_year})."
                )
        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Painting',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'rows': 3,
                    'placeholder': 'Description of the category...',
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Category name must be at least 3 characters long.")
        return name
