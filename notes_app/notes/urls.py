from django.urls import path
from .views import *

urlpatterns = [
    path('', index),  # http://127.0.0.1:8000/notes/
    path('noteshtml/<int:noteshtmlid>/', index_with_html),  # http://127.0.0.1:8000/notes/noteshtml/1/
    path('tamp/', tamp)
]
