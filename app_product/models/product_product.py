from django.db import models

import datetime

class Product_Product(models.Model):
    message_main_attachment_id = models.IntegerField()
    default_code = models.CharField(max_length=10)
    active = models.BooleanField()
    product_tmpl_id = models.IntegerField()
    barcode = models.CharField(max_length=10)
    combination_indices = models.CharField(max_length=10)
    volume= models.FloatField()
    weight= models.FloatField()
    can_image_variant_1024_be_zoomed= models.BooleanField()
    create_uid= models.IntegerField()
    create_date= models.DateTimeField(auto_now_add=True)
    write_uid= models.CharField(max_length=10)
    write_date= models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'product_product'
