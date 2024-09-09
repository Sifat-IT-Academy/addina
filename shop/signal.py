from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductComment, Product


@receiver(pre_save, sender=ProductComment)
def valid_order(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    print(product)

    # if instance.quantity > inventory_item.quantity:
    #     raise Exception("There are not enough items in the inventory.")