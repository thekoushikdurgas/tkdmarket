# Generated by Django 3.2.5 on 2021-12-22 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0012_customerpayment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpayment',
            name='usercarddate',
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='usercardmonth',
            field=models.CharField(default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='usercardyear',
            field=models.CharField(default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
    ]
