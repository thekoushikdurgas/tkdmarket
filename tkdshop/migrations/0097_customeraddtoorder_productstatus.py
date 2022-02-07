# Generated by Django 3.2.5 on 2022-01-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0096_remove_customeraddtoorder_productstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddtoorder',
            name='productstatus',
            field=models.CharField(choices=[['Pending', 'Pending'], ['Accepted', 'Accepted'], ['Packed', 'Packed'], ['Shipped', 'Shipped'], ['On The Way', 'On The Way'], ['Delivered', 'Delivered'], ['Cancel', 'Cancel'], ['Returned', 'Returned'], ['Refunded', 'Refunded']], default='Pending', max_length=150),
        ),
    ]
