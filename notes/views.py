from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Notes
from .forms import NotesForm

# @login_required(login_url="/admin")
# def listNotes(request):
#     notes = Notes.objects.all()
#     return render(request, 'notes/notes.html', {'notes':notes})

def listNote(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("The Note doesn't exist.")
    return render(request, 'notes/notesdetail.html', {'note':note})

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name= "notes"
    template_name="notes/notes.html"
    login_url="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()
    
# class NotesDetailView(DetailView):
#     model = Notes
#     content_object_name = "notes"
#     template_name="notes/notesdetail.html"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/notes/viewnotes'
    # fields = ['title', 'text']
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/viewnotes'
    # fields = ['title', 'text']
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/notes/viewnotes"
    template_name="notes/notes_delete.html"