from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Notes


def index(request):
    notes = Notes.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})
