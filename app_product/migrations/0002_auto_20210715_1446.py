# Generated by Django 2.0.7 on 2021-07-15 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_product',
            name='write_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 14, 46, 25, 661772)),
        ),
    ]
