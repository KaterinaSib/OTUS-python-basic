from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('list/', views.UserListView.as_view(), name='list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
]
