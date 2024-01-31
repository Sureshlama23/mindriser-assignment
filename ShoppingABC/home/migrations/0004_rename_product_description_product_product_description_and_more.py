# Generated by Django 5.0.1 on 2024-01-31 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_brand_brand_slug_category_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_description',
            new_name='product_description',
        ),
        migrations.AlterField(
            model_name='brand',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.brand'),
        ),
    ]
