# Generated by Django 3.2.5 on 2021-12-28 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0014_auto_20211228_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.SlugField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
