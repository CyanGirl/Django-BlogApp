from django import forms
from .models import Posts, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'body', 'image')
        widgets={
            'body':forms.Textarea(attrs={'style':'height:30vh'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('author', 'description')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description':forms.TextInput(attrs={'placeholder': 'Message'})
            }

