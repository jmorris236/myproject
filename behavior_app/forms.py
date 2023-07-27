# behavior_app/forms.py

from django import forms
from .models import Note, Student


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['behavior', 'note', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class AddStudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']
