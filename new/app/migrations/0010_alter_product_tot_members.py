# Generated by Django 4.2.13 on 2024-08-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_tot_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tot_members',
            field=models.IntegerField(null=True),
        ),
    ]
