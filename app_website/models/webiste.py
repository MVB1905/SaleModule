from django.db import models

import datetime

class Website(models.Model):
    id = models.IntegerField(primary_key=True) # ID
    name = models.CharField(max_length=100) # tên website
    domain = models.CharField(max_length=100) # Website domain
    company_id = models.IntegerField() # Công ty
    default_lang_id = models.IntegerField() # Ngôn ngữ mặc định
    auto_redirect_lang = models.BooleanField() # Tự động chuyển ngôn ngữ
    social_twitter = models.CharField(max_length=100)
    social_facebook = models.CharField(max_length=100)
    social_github = models.CharField(max_length=100)
    social_linkedin = models.CharField(max_length=100)
    social_youtube = models.CharField(max_length=100)
    social_instagram = models.CharField(max_length=100)
    google_analytics_key = models.CharField(max_length=100) # Khóa
    google_management_client_id = models.CharField(max_length=100) # Google Client ID - Id khách hàng google
    google_management_client_secret = models.CharField(max_length=100) # Google client secret -
    google_maps_api_key = models.CharField(max_length=100) # Google maps api key
    user_id = models.IntegerField() # Public user Người dùng công cộng (Bình thường)
    cdn_activated = models.BooleanField() # content delivery network CDN
    cdn_url = models.CharField(max_length=100) # CDN Base url
    cdn_filters = models.CharField(max_length=100) # CDN Filters
    homepage_id = models.IntegerField() # Trang chủ
    theme_id = models.IntegerField() # Chủ đề
    specific_user_account = models.BooleanField() # Tài khoản người dùng cụ thể
    auth_signup_uninvited = models.CharField(max_length=100) # Tài khoản khách hàng
    website_form_enable_metadata = models.BooleanField() # Technical data on contact form
    create_uid = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uid = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất

    class Meta:
        db_table = 'webiste'
