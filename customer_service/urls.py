from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customer_service/login.html'), name='login'),
]   