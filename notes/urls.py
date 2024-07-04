from django.urls import path

from . import views

urlpatterns = [
    path('viewnotes', views.listNotes, name='notes.listNotes'),
    path('viewnote/<int:pk>', views.listNote, name='notes.viewnote'),
]