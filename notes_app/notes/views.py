from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notes, Categories
from .forms import CreateNoteForm, NoteForm


@login_required
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


def note_detail_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = CreateNoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Notes, id=note_id, author=request.user)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Нотатку успішно оновлено!')
            return redirect('index')
    else:
        form = CreateNoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'note': note, 'form': form})


@login_required
def edit_note_view(request, id):
    note = get_object_or_404(Notes, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Нотатку успішно оновлено!')
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})


def note_detail_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_detail', pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note, 'form': form})
