# Generated by Django 5.0.1 on 2024-02-11 09:48

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='value',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None),
        ),
    ]
