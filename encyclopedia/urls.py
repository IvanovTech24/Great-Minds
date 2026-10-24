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
    ])),
    path('eras/', include([
        path('', views.EraListView.as_view(), name='eras'),
        path('create/', views.EraCreateView.as_view(), name='era_create'),
        path('<int:pk>/', include([
            path('', views.EraDetailView.as_view(), name='era_detail'),
            path('edit/', views.EraUpdateView.as_view(), name='era_edit'),
            path('delete/', views.EraDeleteView.as_view(), name='era_delete'),
        ]))
    ])),
    path('quotes/', include([
        path('create/', views.QuoteCreateView.as_view(), name='quote_create'),
    ])),
    path('influences/', include([
        path('create/', views.InfluenceCreateView.as_view(), name='influence_create')
    ]))
]