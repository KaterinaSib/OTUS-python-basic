"""
URL configuration for zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = 'meters'

urlpatterns = [
    path('list/', views.MeterListView.as_view(), name='meter_list'),
    path('meter/<int:pk>/', views.MeterDetailView.as_view(), name='meter_detail'),
    path('create/', views.MeterCreateView.as_view(), name='meter_create'),
    path('update/<int:pk>/', views.MeterUpdateView.as_view(), name='meter_update'),
    path('delete/<int:pk>/', views.MeterDeleteView.as_view(), name='meter_delete'),
    path('addresses/list/', views.AddressListView.as_view(), name='address_list'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('addresses/create/', views.AddressCreateView.as_view(), name='address_create'),
    path('addresses/update/<int:pk>/', views.AddressUpdateView.as_view(), name='address_update'),
    path('addresses/delete/<int:pk>/', views.AddressDeleteView.as_view(), name='address_delete'),
]
