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
    ])),
    path('categories/', include([
        path('', views.CategoryListView.as_view(), name='categories'),
        path('create/', views.CategoryCreateView.as_view(), name='category_create'),
        path('<int:pk>/', include([
            path('edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
            path('delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
        ]))
    ])),
]