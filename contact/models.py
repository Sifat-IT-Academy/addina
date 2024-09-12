from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()
    phone=models.CharField(max_length=15,blank=True,null=True)
    birthday=models.DateField(null=True, blank=True) 
    message = models.TextField()
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
