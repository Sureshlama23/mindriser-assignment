# Generated by Django 5.0.1 on 2024-01-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_employeeinfo_email_alter_employeeinfo_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employeeinfo',
            name='password',
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='photo',
            field=models.ImageField(upload_to='Employee_image'),
        ),
    ]
