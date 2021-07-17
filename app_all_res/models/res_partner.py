from django.db import models

import datetime

class Res_partner(models.Model):
    id = models.IntegerField(primary_key=True) # ID
    name = models.CharField(max_length=100)
    company_id = models.IntegerField()
    display_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    title = models.IntegerField()
    parent_id = models.IntegerField() # Related company 0- công ty liên quan
    ref = models.CharField(max_length=100) # Tham chiếu
    lang = models.CharField(max_length=100) # Ngôn ngữ
    tz = models.CharField(max_length=100) # # Múi giờ
    user_id = models.IntegerField() # Nhân viên bán hàng
    vat = models.CharField(max_length=100) # Tax id
    website = models.CharField(max_length=100) # Website link đường dẫn website
    comment = models.TextField() # ghi chú
    credit_limit = models.FloatField() # Giới hạn tín dụng / Hạn mức tín dụng
    active = models.BooleanField() # Hooạt dộng
    employee = models.BooleanField() # Là nhân viên
    function = models.CharField(max_length=100) # Vị trí công việc
    type = models.CharField(max_length=100) # Kiểu địa chỉ
    street = models.CharField(max_length=100) # Đường
    street2 = models.CharField(max_length=100) #
    zip = models.CharField(max_length=100) # Zip
    city = models.CharField(max_length=100) # Thành phố
    state_id = models.IntegerField() # trạng thái
    country_id = models.IntegerField() # Mã quốc gia
    partner_latitude = models.FloatField() #
    partner_longitude = models.FloatField() # geo longitude
    email = models.CharField(max_length=100) # Email
    phone = models.CharField(max_length=100) # Phone
    mobile = models.CharField(max_length=100) # điện thoại di động
    is_company = models.BooleanField() # là 1 công ty
    industry_id = models.IntegerField() # Công nghiệp
    color = models.IntegerField() # CHỉ mục màu
    partner_share = models.BooleanField() # Partner share
    commenercial_partner_id = models.IntegerField() # Thực tế thương mại
    commenercial_company_name = models.CharField(max_length=100) # company name entity
    company_name = models.CharField(max_length=100) # Tên công ty
    message_main_attachment_id = models.IntegerField() # main attachment Đính kèm
    email_normalized = models.CharField(max_length=100) # normalized email email bình thường hóa
    message_bounce = models.IntegerField() # Bounce
    signup_token = models.CharField(max_length=100) # Signup token đăng ký mã thông báo
    signup_type = models.CharField(max_length=100) # Kiểu
    signup_expiration = models.DateTimeField() # hết hạn đăng ký
    partner_gid = models.IntegerField() # company database Id
    additional_info = models.CharField(max_length=100) #
    phone_sanitized = models.CharField(max_length=100) # sanitized number
    team_id = models.IntegerField() # Đội ngũ bán hàng
    debit_limit = models.FloatField() # giới hạn phải trả
    last_time_entries_checked = models.DateTimeField() # Hóa đơn và thanh toán mới nhất
    invoice_warn = models.CharField(max_length=100) # Hóa đơn
    invoice_warn_msg = models.CharField(max_length=100) # tin nhắn cho hóa đơn
    supplier_rank = models.IntegerField() # Xếp hạng nhà cung cấp
    customer_rank = models.IntegerField() # Xếp hạng khách hàng
    sale_warn = models.CharField(max_length=100) # Cảnh báo bán hàng
    sale_warn_msg = models.TextField() # Tin nhắn cho đơn hàng bán hàng
    website_id = models.IntegerField()
    is_published = models.BooleanField() # được công bố                                     FK: website
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất

    class Meta:
        db_table = 'res_partner'