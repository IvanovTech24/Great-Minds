from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from accounts.forms import RegisterForm, LoginForm, ProfileEditForm
from accounts.models import Profile


UserModel = get_user_model()


class RegisterCustomUserView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'accounts/custom_user/register.html'
    success_url = reverse_lazy('accounts:login')


class LoginCustomUserView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/custom_user/login.html'


class LogoutCustomUserView(LogoutView):
    next_page = reverse_lazy('core:home')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/profile-detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile/profile-edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile/profile-delete.html'
    success_url = reverse_lazy('core:home')

    def get_object(self, queryset=None):
        return self.request.user.profile
