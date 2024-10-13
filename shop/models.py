from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.name}"




class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=3,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    description = RichTextField()
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/product')
    main_information = models.CharField(max_length=100)
    weight = models.FloatField()
    dimension = models.TextField()
    purchased_place = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    shipping = models.BigIntegerField()
    care_info = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
    
class ProductComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = IntegerRangeField(min_value=1, max_value=5, default=3)

class Wishlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
