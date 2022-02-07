# Generated by Django 3.2.5 on 2022-01-03 19:58

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0070_customeraddtocart_one_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddtocart',
            name='one_price',
            field=computed_property.fields.ComputedDecimalField(compute_from='oneprice', decimal_places=2, default='0', editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customeraddtocart',
            name='total_price',
            field=computed_property.fields.ComputedDecimalField(compute_from='totalprice', decimal_places=2, default='0', editable=False, max_digits=10),
        ),
    ]