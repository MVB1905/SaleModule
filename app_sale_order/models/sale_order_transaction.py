from django.db import models

import datetime

class Sale_order_transaction(models.Model):
    sale_order_id = models.IntegerField() # FK: sale_order
    transaction_id = models.IntegerField()  # FK: payment_transaction


    class Meta:
        db_table = 'sale_order_transaction'