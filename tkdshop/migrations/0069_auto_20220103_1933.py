# Generated by Django 3.2.5 on 2022-01-03 14:03

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0068_customeraddtocart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddtocart',
            name='Productquantity',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='customeraddtocart',
            name='total_price',
            field=computed_property.fields.ComputedCharField(compute_from='totalprice', default='0', editable=False, max_length=150),
        ),
    ]