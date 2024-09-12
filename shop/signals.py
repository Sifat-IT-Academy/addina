from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import ProductComment, Product


@receiver(post_save, sender=ProductComment)
@receiver(post_delete, sender=ProductComment)
def update_product_rating(sender, instance, **kwargs):
    product = instance.product
    
    comments = product.productcomment_set.all()
    if comments.exists():
        average_rating = sum(comment.rating for comment in comments) / comments.count()
    else:
        average_rating = 0
    product.rating = round(average_rating)
    product.save()