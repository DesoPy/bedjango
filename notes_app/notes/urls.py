from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', index, name='index'),  # http://127.0.0.1:8000/index/
    path('create/', create_note_view, name='create_note'),
    path('note/<int:pk>/', views.note_detail_view, name='note_detail'),
    path('note/<int:id>/edit/', views.edit_note_view, name='edit_note'),
    path('notes/delete/<int:id>', views.delete_note_view, name='delete_note'),
]
