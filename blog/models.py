from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from django.utils.translation import gettext_lazy as _


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    
class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")

