# Generated by Django 3.2.5 on 2022-02-06 20:15

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0153_auto_20220207_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productcatagory',
            field=computed_property.fields.ComputedCharField(compute_from='product_catagory', editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='productcatagory2',
            field=computed_property.fields.ComputedCharField(compute_from='product_catagory2', editable=False, max_length=150),
        ),
    ]
