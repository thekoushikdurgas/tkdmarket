# Generated by Django 3.2.5 on 2022-01-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0121_auto_20220131_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory_id',
            field=models.CharField(default='3', max_length=150),
        ),
    ]
