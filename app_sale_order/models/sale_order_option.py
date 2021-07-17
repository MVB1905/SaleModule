from django.db import models

import datetime

class Sale_order_option(models.Model):
    id = models.IntegerField(primary_key=True) # Id
    order_id = models.IntegerField() # Tham chiếu đơn hàng             FK: sale_order
    line_id = models.IntegerField() # Id dòng                          FK: sale_order_line
    name = models.TextField() # Mô tả
    product_id = models.IntegerField() # Mã sản phẩm                   FK: product_product
    price_unit = models.FloatField() # Đơn giá
    discount = models.FloatField() # Giảm giá %
    uom_id = models.IntegerField() # Đơn vị đo lường                   FK: uom_uom
    quantity = models.FloatField() # Số lượng
    sequence = models.IntegerField() # Trình tự
    create_uid = models.IntegerField() # Tạo bởi ai                    FK: res_users
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần sửa gần nhất bởi ai        FK: res_users
    write_date = models.DateTimeField() # Lần sửa gần nhất vào ngày nào

    class Meta:
        db_table = 'sale_order_option'