# Generated by Django 2.0.7 on 2021-07-15 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_auto_20210715_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_product',
            name='write_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 19, 52, 39, 509099)),
        ),
    ]