# Generated by Django 3.2.5 on 2021-12-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0044_auto_20211230_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='warranty',
            field=models.PositiveIntegerField(),
        ),
    ]