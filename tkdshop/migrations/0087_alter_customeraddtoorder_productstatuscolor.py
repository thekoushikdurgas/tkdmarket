# Generated by Django 3.2.5 on 2022-01-23 19:06

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0086_auto_20220123_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddtoorder',
            name='productstatuscolor',
            field=computed_property.fields.ComputedCharField(compute_from='productstatus_color', editable=False, max_length=150),
        ),
    ]
