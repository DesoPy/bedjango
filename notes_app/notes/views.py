from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Notes
from .forms import CreateNoteForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


def index(request):
    notes = Notes.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes-list')
    else:
        form = CreateNoteForm()

    return render(request, 'notes/create_note.html', {'form': form})


class NoteDetailView(DetailView):
    model = Notes
    template_name = 'notes/note_detail.html'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = ['title', 'text', 'reminder', 'category']
    template_name = 'notes/note_update.html'
    success_url = reverse_lazy('index')


def edit_note(request, pk):
    note = Notes.objects.get(pk=pk)
    form = CreateNoteForm(instance=note)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('edit_note', pk=pk)
    return render(request, 'notes/note_update.html', {'form': form})

