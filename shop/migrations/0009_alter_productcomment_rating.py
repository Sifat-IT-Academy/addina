# Generated by Django 5.1 on 2024-09-25 11:38

import shop.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_productcomment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='rating',
            field=shop.models.IntegerRangeField(default=3),
        ),
    ]
