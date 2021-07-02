from django.forms import ModelForm
from .models import Author
from django import forms

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=['picture','bio']
        widgets={
            'bio':forms.TextInput(attrs={'placeholder':"Tell us something about yourself..."}),
        }
        labels={
            'bio':"",
            'picture':"Profile Image : "
        }