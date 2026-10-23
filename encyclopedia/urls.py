from django.urls import path, include
from encyclopedia import views

app_name = 'encyclopedia'

urlpatterns = [
    path('people/', include([
        path('', views.PersonListView.as_view(), name='people'),
        path('create/', views.PersonCreateView.as_view(), name='create'),
        path('<slug:slug>/', include([
            path('', views.PersonDetailView.as_view(), name='detail'),
            path('edit/', views.PersonUpdateView.as_view(), name='edit'),
            path('delete/', views.PersonDeleteView.as_view(), name='delete'),
        ])),
    ]))
]