from django.db import models

import datetime

class Sale_order(models.Model):
    message_main_attachment_id = models.IntegerField() #                                FK - ir_attachment
    access_token = models.CharField(max_length=10) # Bảo mật
    campaign_id = models.IntegerField() # Chiến dịch -                                  FK - utm_campaign
    source_id = models.IntegerField() # Nguồn -                                         FK - utm_source
    medium_id = models.IntegerField() # Trung bình -                                    FK - utm_medium
    name = models.CharField(max_length=10) # Tham chiếu đặt hàng - Mã sản phẩm
    origin = models.CharField(max_length=10) # Nguồn tài liệu
    client_order_ref = models.CharField(max_length=10) # Tham chiếu mã khách hàng
    reference = models.CharField(max_length=10) # Tham chiếu chính sách thanh toán
    state = models.CharField(max_length=10) # Trạng thái
    date_order = models.DateTimeField() # Ngày đặt hàng
    validity_date = models.DateTimeField() # Hết hạn
    require_signature = models.BooleanField() # Chữ ký số
    require_payment = models.BooleanField() # Chính sách thanh toán trực tuyến
    user_id = models.IntegerField() # Người bán                                     -   FK - res_users
    partner_id = models.IntegerField() # Khách hàng -                                   FK - res_partner
    partner_invoice_id = models.IntegerField() # Địa chỉ hóa đơn -                      FK - res_partner
    partner_shipping_id = models.IntegerField() # Địa chỉ giao hàng                     FK - res_partner
    pricelist_id = models.IntegerField() # Danh sách giá - FK - Product_pricelist
    analytic_account_id = models.IntegerField() # Tài khoản phân tích -                 FK - account_analytic_account
    invoice_status = models.CharField(max_length=10) # Trạng thái hóa đơn
    note = models.TextField() # Ghi chú từ khóa và điều kiện
    amount_untaxed = models.FloatField() # Giá trước thuế
    amount_tax = models.FloatField() # Giá thuế
    amount_total = models.FloatField() # Tổng giá: Giá trước thuế và thuế
    currency_rate = models.FloatField() # Tỷ giá tiền tệ
    payment_term_id = models.IntegerField() # Chính sách thanh toán -                   FK - account_payment_term
    fiscal_position_id  = models.FloatField() # Vị thế tài chính                        FK - account_fiscal_position
    company_id = models.IntegerField() # Công ty -                                      FK - res_company
    team_id = models.IntegerField() # Mã nhóm bán hàng -                                FK - crm_team
    signed_by = models.CharField(max_length=10) # Ký bởi ai
    signed_on = models.DateTimeField() # Ký vào lúc nào
    commitment_date = models.DateTimeField() # Ngày giao hàng
    sale_order_template_id = models.IntegerField() # Mẫu báo giá -                      FK - sale_order_template
    sale_description = models.CharField(max_length=10) # Kiểu tài khoản
    create_uit = models.IntegerField() # Tạo bởi                                        FK - res_user
    create_date = models.DateTimeField() # Ngày tạo
    write_uit = models.IntegerField() # Lần thay đổi gần nhất bởi ai                    FK - res_users
    write_date = models.DateTimeField() # ngày của lần thay đổi gần nhất

    class Meta:
        db_table = 'sale_order'