# Generated by Django 3.2.5 on 2022-02-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0133_auto_20220202_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productid',
            field=models.CharField(default='xBMqUA37UDTcOwkep2Ca', max_length=150),
        ),
    ]