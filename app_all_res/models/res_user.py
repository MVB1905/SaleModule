from django.db import models

import datetime

class Res_users(models.Model):
    id = models.IntegerField(primary_key=True) # ID
    active = models.BooleanField() # Trạng thái hoạt động
    login = models.CharField(max_length=100) # Tên đăng nhập
    password = models.CharField(max_length=100) # Pass
    company_id = models.IntegerField() # Công ty                                        FK: res_company
    partner_id = models.IntegerField() #                                                FK: res_partner
    signature = models.TextField() # Email chữ ký
    action_id = models.IntegerField() # Hành động
    share = models.BooleanField() # Chia sẻ người dùng
    alias_id = models.CharField(max_length=100) # Bí danh                                             FK: mail_alias
    notification_type = models.CharField(max_length=100) # Thông báo
    out_of_office_message = models.CharField(max_length=100) # Trạng thái trò chuyện
    sale_team_id = models.IntegerField() # Nhóm bán hàng của người dùng                 FK: crm_team
    website_id = models.IntegerField() # Website                                        FK: website
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất

    class Meta:
        db_table = 'res_users'