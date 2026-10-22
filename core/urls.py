from django.urls import path
from core import views


app_name = 'core'


urlpatterns = [
    path('', views.home_page_view, name='home')
]
