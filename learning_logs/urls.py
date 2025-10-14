"""Defines URL's for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page.
    path('', views.index, name='index'),
    # Displaying topics.
    path('topics/', views.topics, name='topics'),
    # Specific topic page.
    path('topics/<int:topic_id>/', views.topic, name='topic')
]