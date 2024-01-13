# Generated by Django 5.0.1 on 2024-01-11 18:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_employeeinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]