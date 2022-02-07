# Generated by Django 3.2.5 on 2021-12-29 10:09

from django.db import migrations, models
import multiselectfield.db.fields
import tkdshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdshop', '0041_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=150)),
                ('product_gender', multiselectfield.db.fields.MultiSelectField(choices=[['all', 'All'], ['male', 'Male'], ['female', 'Female'], ['kid', 'Kids'], ['others', 'Others']], max_length=26)),
                ('brand', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='customer/pic/default.jpg', null=True, upload_to=tkdshop.models.productpath)),
                ('catagory_name', models.ManyToManyField(to='tkdshop.Category')),
            ],
            options={
                'db_table': 'Productlist',
            },
        ),
    ]