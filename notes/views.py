from django.shortcuts import render
from django.http import Http404

from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes
from .forms import NotesForm

def listNotes(request):
    notes = Notes.objects.all()
    return render(request, 'notes/notes.html', {'notes':notes})

def listNote(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("The Note doesn't exist.")
    return render(request, 'notes/notesdetail.html', {'note':note})


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/viewnotes'
    # fields = ['title', 'text']
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/viewnotes'
    # fields = ['title', 'text']
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/notes/viewnotes"
    template_name="notes/notes_delete.html"