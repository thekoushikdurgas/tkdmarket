# Generated by Django 3.2.5 on 2022-01-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0095_remove_product_catagoryname_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraddtoorder',
            name='productstatus',
        ),
    ]
