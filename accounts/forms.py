from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import Profile


UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            'placeholder': 'Enter your email',
        })
    )

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                'placeholder': 'Choose a username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            'placeholder': 'Confirm password'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            'placeholder': 'Password'
        })


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'w-full p-2 bg-gray-700 border border-gray-600 rounded text-white focus:outline-none focus:border-amber-500',
            }),
        }
