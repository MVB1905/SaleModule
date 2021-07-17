from django.db import models

import datetime

class Sale_order_template(models.Model):
    id = models.IntegerField(primary_key=True) # Id
    name = models.CharField(max_length=10) # Mẫu báo giá
    note = models.TextField() # Ghi chú từ khóa và điều kiện
    number_or_days = models.IntegerField() # Thời hạn báo giá
    require_signature = models.BooleanField() # Yêu cầu chữ ký trực tuyến
    require_payment = models.BooleanField() # Yêu cầu thanh toán
    mail_template_id = models.IntegerField() # Thư xác nhận            FK: mail_template
    active = models.BooleanField() # Hoạt động
    company_id = models.IntegerField() # Công ty                       FK: res_company
    create_uid = models.IntegerField() # Tạo bởi ai                    FK: res_users
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần sửa gần nhất bởi ai        FK: res_users
    write_date = models.DateTimeField() # Lần sửa gần nhất vào ngày nào

    class Meta:
        db_table = 'sale_order_template'