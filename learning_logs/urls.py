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
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Adding new topic page.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Adding new entry page.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit entry page.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]