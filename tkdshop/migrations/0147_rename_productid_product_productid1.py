# Generated by Django 3.2.5 on 2022-02-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0146_alter_product_productid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productid',
            new_name='productid1',
        ),
    ]
