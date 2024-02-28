# Generated by Django 5.0.2 on 2024-02-27 07:56

import autoslug.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='brand_name', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='category_name', unique=True)),
                ('image', models.ImageField(upload_to='Category_img')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('shipping_fee', models.IntegerField(default=50)),
                ('subtotal', models.PositiveIntegerField(default=0)),
                ('ordered_date', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Deliverd', 'Deliverd'), ('Cancel', 'Cancel')], default='Pending', max_length=20)),
                ('payment_status', models.CharField(choices=[('Not Done', 'Not Done'), ('Done', 'Done')], default='Not Done', max_length=20, null=True)),
            ],
            options={
                'ordering': ['-ordered_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.CharField(max_length=100)),
                ('selling_price', models.PositiveIntegerField(default=1)),
                ('discount_price', models.PositiveIntegerField(default=1)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='product_img')),
                ('product_slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='product_name', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
