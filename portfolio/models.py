from django.db import models
from ckeditor.fields import RichTextField
from account.models import User



class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
        

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Portfolio(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
    

