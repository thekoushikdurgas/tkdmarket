# Generated by Django 3.2.5 on 2022-02-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0142_alter_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productid',
            field=models.CharField(default='oAV21bTXX4atASSif1qq', max_length=150),
        ),
    ]
