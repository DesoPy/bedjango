"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from notes.views import *
from notes import views


urlpatterns = [
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    path('notes/', include('notes.urls')),   # http://127.0.0.1:8000/notes/
    path('index/', index),   # http://127.0.0.1:8000/index/
    path('', views.index, name='notes-list'),
    path('create-note/', views.create_note, name='create-note'),
    path('notes/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/note/<int:pk>/edit/', views.edit_note, name='edit-note'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEIA_URL, document_root=settings.MEDIA_ROOT)
