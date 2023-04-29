from django import forms
from .models import Notes


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminder', 'category']
