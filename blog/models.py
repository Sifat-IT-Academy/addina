from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from django.utils.translation import gettext_lazy as _

class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(BlogTag,related_name='blog',null=True,blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def comments_count(self):
        # pass
        return self.comments.count()

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    
class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")


class Blog_details(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    detail_content = RichTextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return f"Details for {self.blog.title}"
    
