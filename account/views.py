from django.shortcuts import redirect, render
from django.views.generic import View
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


class RegistrationView(View):
    template_name = "authtenticate/sign-up.html"
    form_class = RegistrationForm

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home-page')
        return render(request, self.template_name, {'form':form})
    
    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name, {'form':form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Siz akkauntdan chiqdingiz")
        return redirect(reverse('login-page'))
    
class LoginView(View):
    template_name = "authtenticate/login.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                messages.error(request, "username yoki parolingiz notog'ri !")
        else:
            messages.error(request, "Forma notog'ri to'ldirilgan")
        
        return render(request, self.template_name, context={'form': form})
def profile_view(request):
    return render(request, "profile.html")