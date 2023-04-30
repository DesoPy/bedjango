from django import forms
from .models import Categories, Notes


class CreateNoteForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label=None)

    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminder', 'category']

    def save(self, commit=True):
        note = super(CreateNoteForm, self).save(commit=False)
        note.title = self.cleaned_data['title']
        note.text = self.cleaned_data['text']
        note.reminder = self.cleaned_data['reminder']
        note.category = self.cleaned_data['category']
        if commit:
            note.save()
        return note
