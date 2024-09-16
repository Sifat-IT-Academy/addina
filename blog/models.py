from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogTag, related_name='blogs')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

class BlogComment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")

    def __str__(self):
        return f"Comment by {self.user} on {self.blog}"
