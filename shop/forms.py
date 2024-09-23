from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['name', 'email', 'comment', 'rating']