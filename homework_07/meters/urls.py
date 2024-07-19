from django.urls import path
from . import views


app_name = 'meters'

urlpatterns = [
    path('list/', views.MeterListView.as_view(), name='meter_list'),
    path('meter/<int:pk>/', views.MeterDetailView.as_view(), name='meter_detail'),
    path('create/', views.MeterCreateView.as_view(), name='meter_create'),
    path('meter/<int:pk>/data_create/', views.MeterDataCreateView.as_view(), name='meter_data_create'),
    path('update/<int:pk>/', views.MeterUpdateView.as_view(), name='meter_update'),
    path('delete/<int:pk>/', views.MeterDeleteView.as_view(), name='meter_delete'),
]
