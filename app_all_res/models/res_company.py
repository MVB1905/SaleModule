from django.db import models

import datetime

class Res_company(models.Model):
    id = models.IntegerField(primary_key=True) # ID
    name = models.CharField(max_length=100) # Tên
    partner_id = models.IntegerField() # Công ty mẹ
    currency_id = models.IntegerField() #
    sequence = models.IntegerField() #
    parent_id = models.IntegerField() #
    report_header = models.TextField()
    report_footer = models.TextField()
    logo_web = models.BinaryField()
    account_no = models.CharField(max_length=100) #
    email = models.CharField(max_length=100) #
    phone = models.CharField(max_length=100)
    company_registry = models.CharField(max_length=100) # Đăng ký công ty
    paperformat_id = models.IntegerField() # Định dạng trang
    external_report_layout_id = models.IntegerField() # Mẫu văn bản
    base_onboarding_company_state = models.CharField(max_length=100) # Trạng thái của bước tuân thủ giới thiệu
    font = models.CharField(max_length=100) # Phông
    primary_color = models.CharField(max_length=100) # Màu chủ đạo
    secondary_color = models.CharField(max_length=100) # Màu thứ cấp
    resource_calendar_id = models.IntegerField() # Giờ làm việc mặc định
    partner_gid = models.IntegerField() # ID cơ sở dữ liệu công ty
    snailmail_color = models.BooleanField() # Màu
    snailmail_cover = models.BooleanField() # Thêm trang bìa
    snailmail_duplex = models.BooleanField # Cả hai mặt
    fiscalyear_last_day = models.IntegerField() # Fiscal year last day / Tài chính ngày trước
    fiscalyear_last_month = models.CharField(max_length=100) # Fiscal year last month / Tài chính tháng trước
    period_lock_date = models.DateTimeField() # lock date for non advisers
    fiscalyear_lock_date = models.DateTimeField() # Ngày khóa
    tax_lock_date = models.DateTimeField()  # Ngày khóa thuế
    transfer_account_id = models.IntegerField() # Chuyển khoản liên ngân hàng
    expects_chart_of_accounts = models.BooleanField() # expects a chart of accounts
    chart_template_id = models.IntegerField() # Mẫu biểu đồ
    bank_account_code_prefix = models.CharField(max_length=100) # Tiền tố của tài khoản ngân hàng
    cash_account_code_prefix = models.CharField(max_length=100)   # Tiền tố của tài khoản tiền mặt
    default_cash_difference_income_account_id = models.IntegerField() # Tài khoản thu nhập chênh lệch tiền mặt
    default_cash_difference_expense_account_id = models.IntegerField() # Tài khoản chi phí tiền mặt
    transfer_id_account_code_prefix = models.CharField(max_length=100) # Tiền tố của tài khoản chuyển nhượng
    account_sale_tax_id = models.IntegerField() 
    account_purchase_tax_id = models.IntegerField()
    tax_cash_basis_journal_id = models.IntegerField()
    currency_exchange_journal_id = models.IntegerField()
    anglo_saxon_accounting = models.BooleanField()
    property_stock_account_input_categ_id = models.IntegerField()
    property_stock_account_output_categ_id = models.IntegerField()
    property_stock_valuation_account_id = models.IntegerField()
    tax_exigibility = models.BooleanField()
    account_bank_reconciliation_start = models.DateTimeField()
    incoterm_id = models.IntegerField()
    qr_code = models.BooleanField()
    invoice_is_email = models.BooleanField() # Mặc định gửi hóa đơn tới email
    invoice_is_print = models.BooleanField() # Mặc định in hóa đơn
    account_opening_move_id = models.IntegerField() # Mở mục nhập nhật ký
    account_setup_bank_data_state = models.CharField(max_length=100) # trạng thái của bước tích hợp dữ liệu ngân hàng
    account_setup_fy_data_state = models.CharField(max_length=100) # trạng thái của bước tham gia năm tài chính
    account_setup_coa_state = models.CharField(max_length=100) #  trạng thái của các biểu đồ giới thiệu của bước tài khoản
    account_onboarding_invoice_layout_state = models.CharField(max_length=100) # trạng thái của bước bố trí hóa đơn giới thiệu
    account_onboarding_sample_invoice_state = models.CharField(max_length=100) # trạng thái của bước bố trí mẫu giới thiệu
    account_onboarding_sale_tax_state = models.CharField(max_length=100) # trạng thái của bước thuế bán hàng gia nhập
    account_invoice_onboarding_state = models.CharField(max_length=100) # trạng thái của bảng giới thiệu hóa đơn giới thiệu
    account_dashboard_onboarding_state = models.CharField(max_length=100) # trạng thái của bảng tổng quan tài khoản giới thiệu bảng điều khiển
    invoice_terms = models.TextField() # Mẫu mặc định và điều kiện
    account_default_pos_receivable_account_id = models.IntegerField() # Khoản phải thu mặc định
    expense_accrual_account_id = models.IntegerField() #  tài khoản tích lũy chi phí
    revenue_accrual_account_id = models.IntegerField() # Tài khoản tích lũy doanh thu
    accrual_default_journal_id = models.IntegerField() # Cộng dồn tạp chí mặc định
    payment_acquirer_onboarding_state = models.CharField(max_length=100) # trạng thái của bước tiếp nhận thanh toán giới thiệu
    payment_onboarding_payment_method = models.CharField(max_length=100) # đã chọn phương thức thanh toán giới thiệu
    invoice_is_snailmail = models.BooleanField() # Gửi qua đường bưu điện
    portal_confirmation_sign = models.BooleanField() # Chữ ký số
    portal_confirmation_pay = models.BooleanField() # Thanh toán trực tuyến
    portal_validity_days = models.IntegerField() # giá trị báo giá mặc định
    sale_quotation_onboarding_state = models.CharField(max_length=100) # trạng thái của bảng giới thiệu bán hàng
    state_onboarding_sample_quotation_state = models.CharField(max_length=100) # Trạng thái của bước báo giá mẫu giới thiệu
    sale_onboarding_payment_method = models.CharField(max_length=100) # Giảm giá khi giới thiệu phương thức thanh toán đã chọn
    social_twitter = models.CharField(max_length=100)
    social_facebook = models.CharField(max_length=100)
    social_github = models.CharField(max_length=100)
    social_linkedin = models.CharField(max_length=100)
    social_youtube = models.CharField(max_length=100)
    social_instagram = models.CharField(max_length=100)

    class Meta:
        db_table = 'res_company'