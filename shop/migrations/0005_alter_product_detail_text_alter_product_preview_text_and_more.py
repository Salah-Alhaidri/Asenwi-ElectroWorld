# Generated by Django 5.1.4 on 2025-02-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail_text',
            field=models.TextField(max_length=300, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_text',
            field=models.TextField(max_length=300, verbose_name='Preview Text'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
