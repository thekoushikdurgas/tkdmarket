# Generated by Django 3.2.5 on 2022-01-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0063_auto_20220102_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('catagory_id', models.AutoField(primary_key=True, serialize=False)),
                ('catagory_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Category1list',
            },
        ),
        migrations.AddField(
            model_name='category2',
            name='catagory_name2',
            field=models.CharField(default='', max_length=150),
        ),
    ]
