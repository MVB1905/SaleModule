from django.db import models

import datetime

class Res_currency(models.Model):
    id = models.IntegerField(primary_key=True) # ID
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    rounding = models.FloatField() # Yếu tố làm tròn
    decimal_places = models.IntegerField() # Decimal places
    active = models.BooleanField()
    position = models.CharField(max_length=100) # Vị chí biểu tượng symbol position
    currency_unit_label = models.CharField(max_length=100) # Đơn vị tiền tệ
    currency_subunit_label = models.CharField(max_length=100) # Đơn vị tiền tệ thứ cấp/ Phụ currency subunit
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất
    class Meta:
        db_table = 'res_currency'