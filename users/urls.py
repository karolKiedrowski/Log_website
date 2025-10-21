"""Defines url address templates for users application."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Adding default authentication urls.
    path('', include('django.contrib.auth.urls')),
    # Registry page.
    path('register/', views.register, name='register'),
]