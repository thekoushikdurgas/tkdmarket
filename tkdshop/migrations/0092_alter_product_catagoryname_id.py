# Generated by Django 3.2.5 on 2022-01-25 14:02

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0091_product_catagoryname_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagoryname_id',
            field=computed_property.fields.ComputedCharField(compute_from='catagorynameid', default='', editable=False, max_length=150),
        ),
    ]
