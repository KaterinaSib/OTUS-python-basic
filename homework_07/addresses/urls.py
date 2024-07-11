from django.urls import path
from . import views


app_name = 'addresses'

urlpatterns = [
    path('list/', views.AddressListView.as_view(), name='address_list'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('create/', views.AddressCreateView.as_view(), name='address_create'),
    path('update/<int:pk>/', views.AddressUpdateView.as_view(), name='address_update'),
    path('delete/<int:pk>/', views.AddressDeleteView.as_view(), name='address_delete'),
]
