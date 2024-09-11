from django.db import models
from ckeditor.fields import RichTextField
from account.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    rating = models.FloatField(default=3)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
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


class ProductComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField()
