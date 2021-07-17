from django.db import models

import datetime

class Sale_order_line_invoice_rel(models.Model):
    invoice_line_id = models.IntegerField() # FK: account_move_line
    order_lint_id = models.IntegerField()  # FK: sale_order_line


    class Meta:
        db_table = 'sale_order_line_invoice_rel'