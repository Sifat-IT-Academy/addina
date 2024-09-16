from django.contrib import admin
from django.shortcuts import render
from .models import Blog,BlogCategory,BlogComment,BlogTag
from django.utils.html import format_html

admin.site.register(BlogTag)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("rasm","title","user","created_date","category")
    readonly_fields = ['id']

    def rasm(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("author","email","body","created_at","active","blog")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  
