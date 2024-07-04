from django.shortcuts import render
from django.http import Http404

from .models import Notes

def listNotes(request):
    notes = Notes.objects.all()
    return render(request, 'notes/notes.html', {'notes':notes})

def listNote(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("The Note doesn't exist.")
    return render(request, 'notes/notesdetail.html', {'note':note})
