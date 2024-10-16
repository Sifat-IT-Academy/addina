# Generated by Django 5.1 on 2024-10-14 09:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolio_client_en_portfolio_client_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_details',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio_details',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio_details',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='portfolio_details',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]