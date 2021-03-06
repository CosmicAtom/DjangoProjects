from cProfile import label
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : 'Entry:'}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}