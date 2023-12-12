from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
  
  
class AddBookForm(forms.ModelForm):
    access_no = forms.CharField(required=True)
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)
    status = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta:
        model = Books
        fields = ('access_no', 'title', 'author', 'status', 'location')