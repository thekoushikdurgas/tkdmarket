# Generated by Django 3.2.5 on 2022-01-21 21:49

import computed_property.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0078_auto_20220120_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customeraddtoorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=150)),
                ('Productquantity', models.PositiveIntegerField(default=1000)),
                ('userid', models.CharField(max_length=150)),
                ('addressid', models.CharField(max_length=150)),
                ('paymentid', models.CharField(max_length=150)),
                ('paid', models.BooleanField(default=False)),
                ('productstatus', multiselectfield.db.fields.MultiSelectField(choices=[['Pending', 'Pending'], ['Awaiting Payment', 'Awaiting Payment'], ['Accepted', 'Accepted'], ['Packed', 'Packed'], ['Awaiting Shipment', 'Awaiting Shipment'], ['Shipped', 'Shipped'], ['On The Way', 'On The Way'], ['Awaiting Pickup', 'Awaiting Pickup'], ['Delivered', 'Delivered'], ['Completed', 'Completed'], ['Disputed', 'Disputed'], ['Cancel', 'Cancel'], ['Declined', 'Declined'], ['Refunded', 'Refunded']], default='Pending', max_length=147)),
                ('orderid', computed_property.fields.ComputedCharField(compute_from='order_id', editable=False, max_length=150)),
                ('total_price', computed_property.fields.ComputedDecimalField(compute_from='totalprice', decimal_places=2, default='0', editable=False, max_digits=10)),
                ('one_price', computed_property.fields.ComputedDecimalField(compute_from='oneprice', decimal_places=2, default='0', editable=False, max_digits=10)),
            ],
            options={
                'db_table': 'Customeraddtoorderlist',
            },
        ),
    ]