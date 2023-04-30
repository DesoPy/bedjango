from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Notes, Categories
from .forms import CreateNoteForm


def index(request):
    notes = Notes.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'categories': Categories.objects.all()})


def create_note_view(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, 'Нотатку успішно створено!')
            return redirect('index')
    else:
        form = CreateNoteForm()
    return render(request, 'notes/create_note.html', {'form': form})


