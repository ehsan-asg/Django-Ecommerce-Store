# Generated by Django 5.0.1 on 2024-02-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.ManyToManyField(related_name='pfeature', to='product.feature'),
        ),
    ]