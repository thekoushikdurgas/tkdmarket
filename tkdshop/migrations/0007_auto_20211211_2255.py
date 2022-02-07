# Generated by Django 3.2.5 on 2021-12-11 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0006_auto_20211209_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraddresses',
            name='userphone',
        ),
        migrations.AddField(
            model_name='customerdeatail',
            name='userphone',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
