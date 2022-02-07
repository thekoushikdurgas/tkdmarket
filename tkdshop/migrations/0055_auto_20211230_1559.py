# Generated by Django 3.2.5 on 2021-12-30 10:29

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0054_product_catagory_name_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catagory_name_list',
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=computed_property.fields.ComputedCharField(compute_from='catagorynamelist', editable=False, max_length=150),
        ),
    ]
