# Generated by Django 5.0.1 on 2024-01-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_employeeinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
