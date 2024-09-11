from django.db import models
from account.models import User
from shop.models import Product

# Cart
class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True) # models.BooleanField(default=False, null=False, blank=False)
