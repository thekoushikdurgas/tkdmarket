# Generated by Django 3.2.5 on 2022-02-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0129_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productid',
            field=models.CharField(default='iwnHk8gX7aQl6RAUC4XB', max_length=150),
        ),
    ]
