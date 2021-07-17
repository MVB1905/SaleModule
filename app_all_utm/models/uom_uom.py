from django.db import models

import datetime

class Uom_uom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.IntegerField()
    factor = models.FloatField() # tỉ lệ
    rounding = models.FloatField() # độ chính xác (làm tròn)
    active = models.BooleanField()
    uom_type = models.CharField(max_length=100) # Kiểu
    measure_type = models.CharField(max_length=100) # kiểu đo lường
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất
    class Meta:
        db_table = 'uom_uom'