# Generated by Django 3.2.5 on 2022-02-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0139_alter_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productid',
            field=models.CharField(default='Kq8flx5KESpQJZvNQ6K2', max_length=150),
        ),
    ]
