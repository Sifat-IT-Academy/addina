# Generated by Django 5.0.6 on 2024-09-16 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogtag_remove_blog_tag_alter_blogcomment_blog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.blogcategory'),
        ),
    ]
