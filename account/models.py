from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    

    def clean(self):
        phone_number_pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        if not re.match(phone_number_pattern,self.phone_number):

            raise ValidationError(_("Phone number incorrect"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")



