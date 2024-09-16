from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from django.utils.translation import gettext_lazy as _


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Portfolio Category")
        verbose_name_plural = _("Portfolio Categories")

   
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
