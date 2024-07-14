from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='service_requests/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='service_requests/logout.html'), name='logout'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:pk>/', views.track_request, name='track_request'),
    path('requests/logout/', auth_views.LogoutView.as_view(), name='logout'),
]