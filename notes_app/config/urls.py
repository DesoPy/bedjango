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
from notes.views import index
from notes.views import create_note, NoteDetailView, NoteUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('notes/', include('notes.urls')),
    path('create-note/', create_note, name='create-note'),
    path('notes/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/note/<int:pk>/edit_note/', NoteUpdateView.as_view(), name='edit_note'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEIA_URL, document_root=settings.MEDIA_ROOT)
