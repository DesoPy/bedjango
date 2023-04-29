from django.urls import path
from .views import *
from notes.views import NoteUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('create-note/', create_note, name='create-note'),
    path('notes/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/note/<int:pk>/edit-note/', NoteUpdateView.as_view(), name='edit-note'),
]
