# Generated by Django 3.2.5 on 2021-12-31 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0059_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
    ]
