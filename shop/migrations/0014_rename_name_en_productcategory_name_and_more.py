# Generated by Django 5.1 on 2024-10-13 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_rename_name_productcategory_name_uz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='name_en',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='name_uz',
        ),
    ]
