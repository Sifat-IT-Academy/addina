from django.db import models
from account.models import User
from shop.models import Product

# Cart
class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

# # Coupon
# class Coupon(models.Model):
#     code = models.CharField(max_length=50, unique=True)
#     discount_type = models.CharField(max_length=10, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')])
#     discount_value = models.FloatField()

#     def __str__(self):
#         return self.code
