# Generated by Django 5.0.1 on 2024-01-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='static/bookspdf/'),
        ),
    ]
