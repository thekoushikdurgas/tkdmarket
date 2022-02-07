# Generated by Django 3.2.5 on 2022-01-31 08:59

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0119_product_productcatagory2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producttogether',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=150)),
                ('productid', models.CharField(max_length=150)),
                ('productid1', models.CharField(max_length=150)),
                ('Productquantity', models.PositiveIntegerField(default=1000)),
                ('wishlistid', computed_property.fields.ComputedCharField(compute_from='wishlist_id', editable=False, max_length=150)),
                ('total_price', computed_property.fields.ComputedDecimalField(compute_from='totalprice', decimal_places=2, default='0', editable=False, max_digits=10)),
                ('one_price', computed_property.fields.ComputedDecimalField(compute_from='oneprice', decimal_places=2, default='0', editable=False, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Producttogetherlist',
            },
        ),
    ]
