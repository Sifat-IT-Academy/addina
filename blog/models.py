from django.db import models
from ckeditor.fields import RichTextField
from account.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Images/blog')
    create_date = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(Blog,on_delete=models.CASCADE)