# Generated by Django 3.2.5 on 2022-01-26 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0098_customeraddtoorder_productstatusdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraddtoorder',
            name='productstatusdate',
        ),
    ]
