# Generated by Django 3.2.5 on 2022-01-02 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0062_auto_20220102_0153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category2',
        ),
        migrations.AlterModelTable(
            name='category2',
            table='Category2list',
        ),
    ]
