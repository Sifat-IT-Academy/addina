# Generated by Django 5.1 on 2024-10-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcategory_name_en_blogcategory_name_uz'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='author_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='author_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='body_uz',
            field=models.TextField(null=True),
        ),
    ]
