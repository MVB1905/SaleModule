from django.db import models

import datetime

class Sale_order_template_line(models.Model):
    id = models.IntegerField(primary_key=True) # Id
    sequence = models.IntegerField() # Trình tự
    sale_order_template_id = models.IntegerField() # Mẫu báo giá       FK: sale_order_template
    company_id = models.IntegerField() # Công ty                       FK: res_company
    name = models.TextField() # Mô tả
    product_id = models.IntegerField() # Mã sản phẩm                   FK: product_product
    price_unit = models.FloatField() # Đơn giá
    discount = models.FloatField() # Giảm giá %
    product_uom_qty = models.FloatField() # Số lượng
    product_uom_id = models.IntegerField() # Đơn vị đo lường           FK: uom_uom
    display_type = models.CharField(max_length=max) # Kiểu hiển thị
    create_uid = models.IntegerField() # Tạo bởi ai                    FK: res_users
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần sửa gần nhất bởi ai        FK: res_users
    write_date = models.DateTimeField() # Lần sửa gần nhất vào ngày nào

    class Meta:
        db_table = 'sale_order_template_line'