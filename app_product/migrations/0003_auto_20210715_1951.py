# Generated by Django 2.0.7 on 2021-07-15 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_auto_20210715_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_product',
            name='write_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 19, 50, 48, 313024)),
        ),
    ]
