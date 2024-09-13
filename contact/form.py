from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "content", "phone", "birthday"] 

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        if not name:
            raise forms.ValidationError("Name is required.")
        return name

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content

    # Agar siz telefon raqamining formatini tekshirmoqchi bo'lsangiz
   
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        # Telefon raqamining formatini tekshiradigan yangilangan regex
        if phone and not re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone):
            raise forms.ValidationError("Phone number is in the wrong format.")
        
        return phone