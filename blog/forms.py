from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('author', 'email', 'body')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'placeholder': 'Your Comment Here...'})


class ReplyForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['author', 'email', 'body']
