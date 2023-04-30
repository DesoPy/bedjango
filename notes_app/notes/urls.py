from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),  # http://127.0.0.1:8000/index/
    path('create/', create_note_view, name='create_note'),

]
