from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
]