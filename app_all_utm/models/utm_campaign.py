from django.db import models

import datetime

class Utm_campaign(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.IntegerField() # Người chịu trách nhiệm
    stage_id = models.IntegerField() # Stage
    is_website = models.BooleanField()
    color = models.IntegerField() # Màu chỉ mục
    company_id = models.IntegerField() # Công ty
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất
    class Meta:
        db_table = 'utm_campaign'