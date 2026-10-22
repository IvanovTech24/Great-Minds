from django.urls import path, include
from encyclopedia import views

app_name = 'encyclopedia'

urlpatterns = [
    path('people/', include([
        path('', views.PersonListView.as_view(), name='people'),
        path('<slug:slug>/', views.PersonDetailView.as_view(), name='detail'),
    ]))
]