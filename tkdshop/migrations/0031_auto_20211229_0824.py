# Generated by Django 3.2.5 on 2021-12-29 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0030_opetest_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='catagory_name',
        ),
        migrations.DeleteModel(
            name='opetest',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
