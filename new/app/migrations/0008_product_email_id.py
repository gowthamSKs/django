# Generated by Django 4.2.13 on 2024-08-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_product_cgpa_remove_product_feedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Email_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
