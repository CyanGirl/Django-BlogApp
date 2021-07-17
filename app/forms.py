from django import forms
from .models import Posts, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'body', 'image','categories')
        widgets={
            'body':forms.Textarea(attrs={'style':'height:30vh'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('description',)
        widgets = {
            'description':forms.TextInput(attrs={'placeholder': 'Leave a thought'})
            }

