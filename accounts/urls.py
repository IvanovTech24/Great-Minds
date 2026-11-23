from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterCustomUserView.as_view(), name='register'),
    path('login/', views.LoginCustomUserView.as_view(), name='login'),
    path('logout/', views.LogoutCustomUserView.as_view(), name='logout'),
    path('profile', include([
        path('', views.ProfileDetailView.as_view(), name='profile'),
        path('edit/', views.ProfileEditView.as_view(), name='profile_edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete')
    ]))
]