# Generated by Django 3.2.5 on 2022-01-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0084_alter_customerdeatail_usergender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdeatail',
            name='usergender',
            field=models.CharField(choices=[['all', 'All'], ['male', 'Male'], ['female', 'Female'], ['kid', 'Kids'], ['others', 'Others']], default='male', max_length=150),
        ),
    ]
