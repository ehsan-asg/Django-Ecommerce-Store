# Generated by Django 5.0.1 on 2024-02-14 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.discount'),
        ),
    ]
