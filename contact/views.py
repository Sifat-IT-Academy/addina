from django.shortcuts import render
from .models import Contact
from .bot import send_message
from django.views.generic.edit import FormView
from contact.form import ContactForm
from django.contrib import messages

class ContactFormView(FormView):
    template_name='contact.html'
    form_class = ContactForm
    success_url = '/ru/shop/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        birthday=form.cleaned_data.get('birthday')
        content = form.cleaned_data.get('content')
        text = f"Name : {name}\nEmail : {email}\nPhone number : {phone}\nBirthday : {birthday}\nContent : {content}"
        send_message(text)  
        
        Contact.objects.create(name=name, email=email, content=content,phone=phone,birthday=birthday,user=self.request.user)
        messages.success(self.request, "Sizning so'rovingiz adminga yuborildi.✅")
        return super().form_valid(form)

