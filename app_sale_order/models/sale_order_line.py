from django.db import models

import datetime

class Sale_order_line(models.Model):
    id = models.IntegerField(primary_key=True) # Id
    order_id = models.IntegerField() # Tham chiếu đơn hàng                                              FK: sale_order
    name = models.TextField() # Mô tả
    sequence = models.IntegerField() # Trình tự
    invoice_status = models.CharField(max_length=10) # Trạng thái hóa đơn
    price_unit = models.FloatField() # Đơn giá
    price_subtotal = models.FloatField() # Tổng phụ giá
    price_tax = models.FloatField() # Tổng thuế
    price_total = models.FloatField() # Tổng giá
    price_reduce = models.FloatField() # Giảm giá
    price_reduce_taxinc = models.FloatField() # Giảm giá bao gồm thuê
    price_reduce_taxexcl = models.FloatField() # Giảm giá không bao gồm thuế
    discount = models.FloatField() # Giảm giá %
    product_id = models.IntegerField() # Mã sản phẩm                                                    FK: product_product
    product_uom_qty = models.FloatField() # Số lượng
    product_uom = models.IntegerField() # Đơn vị đo lường                                               FK: uom_uom
    qty_delivered_method = models.CharField(max_length=10) # Phương pháp cập nhật số lượng đã giao
    qty_delivered = models.FloatField() # Số lượng đã giao
    qty_delevered_manual = models.FloatField() # giao hàng thủ công
    qty_to_invoice = models.FloatField() # Số lượng hóa đơn
    qty_invoice = models.FloatField() # Số lượng đã lập trong hóa đơn
    untaxed_amount_invoiced = models.FloatField() # Số tiền được lập trong hóa đơn chưa tính thuế
    untaxed_amount_to_invoice = models.FloatField() # Số tiền chưa tính thuế cho hóa đơn
    salesman_id = models.IntegerField() # Nhân viên bán hàng                                            FK: res_users
    currency_id = models.IntegerField() # Tiền tệ                                                       FK: res_currency
    company_id = models.IntegerField() # Công ty                                                        FK: res_company
    order_partner_id = models.IntegerField # Khách hàng đặt hàng                                        FK: res_partner
    is_expense = models.BooleanField() # Hết hạn or Chi phí
    is_downpayment = models.BooleanField() # Giảm thanh toán
    state = models.CharField(max_length=10) # Trạng thái đơn hàng
    customer_lead = models.FloatField() # Lead time
    display_type = models.CharField(max_length=10) # Kiểu thiển thị
    create_uid = models.IntegerField() # Tạo bởi                                                           FK: res_users
    create_date = models.DateTimeField() # được tạo vào ngày nào
    write_uid = models.IntegerField() # Lần sửa gần nhất bởi ai                                            FK: res_user
    write_date = models.DateTimeField() # Ngày sửa gần nhất

    class Meta:
        db_table = 'sale_order_line'