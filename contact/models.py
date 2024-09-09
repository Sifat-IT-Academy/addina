from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
