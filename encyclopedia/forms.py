from django import forms
from django.core.exceptions import ValidationError
from encyclopedia.models import Person, Era, Quote, Influence


class PersonForm(forms.ModelForm):
    full_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'w-full p-2 bg-gray-600 border border-gra-500 rounded text-gray-400 cursor-not-allowed',
                'readonly': 'readonly',
            }
        ),
        label='Full Name (Auto-generated)'
    )

    class Meta:
        model = Person
        fields = [
            'first_name', 'last_name', 'full_name',
            'birth_year', 'death_year', 'nationality',
            'short_bio', 'biography', 'fun_fact',
            'portrait', 'era'
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Leonardo'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. da Vinci',
                }
            ),
            'birth_year': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. 1452',
                }
            ),
            'death_year': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. 1519',
                }
            ),
            'nationality': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Italian',
                }
            ),
            'short_bio': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'A brief summary...',
                }
            ),
            'biography': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'Full biography...',
                }
            ),
            'fun_fact': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'A curious fact...',
                }
            ),
            'portrait': forms.FileInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                }
            ),
            'era': forms.Select(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                }
            ),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['full_name'].initial = f"{self.instance.first_name} {self.instance.last_name}"


    def clean_death_year(self):
        death_year = self.cleaned_data.get('death_year')
        birth_year = self.cleaned_data.get('birth_year')


        if death_year and birth_year and death_year < birth_year:
                raise ValidationError('Death year cannot be earlier than birth year.')

        return death_year


class EraForm(forms.ModelForm):
    class Meta:
        model = Era
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Renaissance'
                }
            ),
            'start_year': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. 1400'
                }
            ),
            'end_year': forms.NumberInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. 1600'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'rows': 4,
                    'placeholder': 'Description of the era...'
                }
            ),
            'color_hex': forms.TextInput(
                attrs={
                    'class': 'h-10 w-10 p-1 bg-gray-700 border border-gray-600 rounded cursor-pointer focus:outline-none focus:border-amber-500',
                    'type': 'color',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_year = cleaned_data.get('start_year')
        end_year = cleaned_data.get('end_year')

        if start_year and end_year and start_year> end_year:
            self.add_error('end_year', 'End year cannot be earlier than start year.')

        return cleaned_data


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'rows': 3,
                    'placeholder': 'Enter the quote...'
                }
            ),
            'person': forms.Select(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500'
                }
            ),
            'source': forms.TextInput(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'placeholder': 'e.g. Book, Speech',
                }
            ),
        }


class InfluenceForm(forms.ModelForm):
    class Meta:
        model = Influence
        fields = '__all__'
        widgets = {
            'influencer': forms.Select(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500'
                }
            ),
            'influenced': forms.Select(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                    'rows': 3,
                    'placeholder': 'How did they influence each other?',
                }
            ),
        }