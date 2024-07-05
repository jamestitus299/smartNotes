from django.urls import path

from . import views

urlpatterns = [
    path('viewnotes', views.listNotes, name='notes.listNotes'),
    path('viewnote/<int:pk>', views.listNote, name='notes.viewnote'),
    path('new', views.NotesCreateView.as_view(), name='notes.new'),
    path('viewnote/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('viewnote/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),


]