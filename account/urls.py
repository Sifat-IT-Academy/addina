from django.urls import path
from .views import LoginView,LogoutView,RegistrationView, ProfileEditView


urlpatterns = [
  path('login',LoginView.as_view(),name='login-page'),
  path('logout/', LogoutView.as_view(), name='logout-page'),
  path('register/',RegistrationView.as_view(),name='register-page'),
  path('profile/<int:pk>/', ProfileEditView.as_view(),name='profile-page')
]