# Generated by Django 3.2.5 on 2022-01-26 17:47

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0103_remove_customeraddtoorder_productstatusdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddtoorder',
            name='productstatusdate',
            field=computed_property.fields.ComputedCharField(compute_from='product_status_date', default=' | | | | | | | | ', editable=False, max_length=150),
        ),
    ]