from django.urls import path, include
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('works/', include([
        path('', views.WorkListView.as_view(), name='works'),
        path('create/', views.WorkCreateView.as_view(), name='create'),
        path('<slug:slug>/', include([
            path('', views.WorkDetailView.as_view(), name='detail'),
            path('edit/', views.WorkUpdateView.as_view(), name='edit'),
            path('delete/', views.WorkDeleteView.as_view(), name='delete'),
        ]))
    ]))
]