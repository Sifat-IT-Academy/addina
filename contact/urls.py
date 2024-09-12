from django.urls import path
from .views import ContactFormView

urlpatterns = [
    path('contact/',ContactFormView.as_view(),name='contact-page')
]