from django.shortcuts import redirect, render
from django.views.generic import View
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
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
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is not valid.")
        
        return render(request, self.template_name, context={'form': form})