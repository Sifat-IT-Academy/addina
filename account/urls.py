from django.urls import path
from .views import LoginView,LogoutView,sign_up


urlpatterns = [
  path('login',LoginView.as_view(),name='login-page'),
  path('logout/', LogoutView.as_view(), name='logout-page'),
  path('register/',sign_up,name='register-page')
]