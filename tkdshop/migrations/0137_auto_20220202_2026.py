# Generated by Django 3.2.5 on 2022-02-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0136_auto_20220202_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productid',
            field=models.CharField(default='KIAX28RK7Imp9JV1tvmg', max_length=150),
        ),
    ]
