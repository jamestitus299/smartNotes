from django import forms
from .models import Notes

from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError("We only accept notes about Django")
    #     return title