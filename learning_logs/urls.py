"""Defining  URL patterns for learning_logs"""

from msilib.schema import Patch
from unicodedata import name
from zipfile import *
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topic/<int:topic_id>/', views.topic, name='topic')
    # Page for adding a new topic
    path ('new_topic/', views.new_topic, name='new_topic')
]
