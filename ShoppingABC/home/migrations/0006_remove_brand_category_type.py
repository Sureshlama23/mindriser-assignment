# Generated by Django 5.0.1 on 2024-01-31 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category_type',
        ),
    ]
