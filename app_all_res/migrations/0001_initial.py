# Generated by Django 2.0.7 on 2021-07-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Res_company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('partner_id', models.IntegerField()),
                ('currency_id', models.IntegerField()),
                ('sequence', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('report_header', models.TextField()),
                ('report_footer', models.TextField()),
                ('logo_web', models.BinaryField()),
                ('account_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('company_registry', models.CharField(max_length=100)),
                ('paperformat_id', models.IntegerField()),
                ('external_report_layout_id', models.IntegerField()),
                ('base_onboarding_company_state', models.CharField(max_length=100)),
                ('font', models.CharField(max_length=100)),
                ('primary_color', models.CharField(max_length=100)),
                ('secondary_color', models.CharField(max_length=100)),
                ('resource_calendar_id', models.IntegerField()),
                ('partner_gid', models.IntegerField()),
                ('snailmail_color', models.BooleanField()),
                ('snailmail_cover', models.BooleanField()),
                ('fiscalyear_last_day', models.IntegerField()),
                ('fiscalyear_last_month', models.CharField(max_length=100)),
                ('period_lock_date', models.DateTimeField()),
                ('fiscalyear_lock_date', models.DateTimeField()),
                ('tax_lock_date', models.DateTimeField()),
                ('transfer_account_id', models.IntegerField()),
                ('expects_chart_of_accounts', models.BooleanField()),
                ('chart_template_id', models.IntegerField()),
                ('bank_account_code_prefix', models.CharField(max_length=100)),
                ('cash_account_code_prefix', models.CharField(max_length=100)),
                ('default_cash_difference_income_account_id', models.IntegerField()),
                ('default_cash_difference_expense_account_id', models.IntegerField()),
                ('transfer_id_account_code_prefix', models.CharField(max_length=100)),
                ('account_sale_tax_id', models.IntegerField()),
                ('account_purchase_tax_id', models.IntegerField()),
                ('tax_cash_basis_journal_id', models.IntegerField()),
                ('currency_exchange_journal_id', models.IntegerField()),
                ('anglo_saxon_accounting', models.BooleanField()),
                ('property_stock_account_input_categ_id', models.IntegerField()),
                ('property_stock_account_output_categ_id', models.IntegerField()),
                ('property_stock_valuation_account_id', models.IntegerField()),
                ('tax_exigibility', models.BooleanField()),
                ('account_bank_reconciliation_start', models.DateTimeField()),
                ('incoterm_id', models.IntegerField()),
                ('qr_code', models.BooleanField()),
                ('invoice_is_email', models.BooleanField()),
                ('invoice_is_print', models.BooleanField()),
                ('account_opening_move_id', models.IntegerField()),
                ('account_setup_bank_data_state', models.CharField(max_length=100)),
                ('account_setup_fy_data_state', models.CharField(max_length=100)),
                ('account_setup_coa_state', models.CharField(max_length=100)),
                ('account_onboarding_invoice_layout_state', models.CharField(max_length=100)),
                ('account_onboarding_sample_invoice_state', models.CharField(max_length=100)),
                ('account_onboarding_sale_tax_state', models.CharField(max_length=100)),
                ('account_invoice_onboarding_state', models.CharField(max_length=100)),
                ('account_dashboard_onboarding_state', models.CharField(max_length=100)),
                ('invoice_terms', models.TextField()),
                ('account_default_pos_receivable_account_id', models.IntegerField()),
                ('expense_accrual_account_id', models.IntegerField()),
                ('revenue_accrual_account_id', models.IntegerField()),
                ('accrual_default_journal_id', models.IntegerField()),
                ('payment_acquirer_onboarding_state', models.CharField(max_length=100)),
                ('payment_onboarding_payment_method', models.CharField(max_length=100)),
                ('invoice_is_snailmail', models.BooleanField()),
                ('portal_confirmation_sign', models.BooleanField()),
                ('portal_confirmation_pay', models.BooleanField()),
                ('portal_validity_days', models.IntegerField()),
                ('sale_quotation_onboarding_state', models.CharField(max_length=100)),
                ('state_onboarding_sample_quotation_state', models.CharField(max_length=100)),
                ('sale_onboarding_payment_method', models.CharField(max_length=100)),
                ('social_twitter', models.CharField(max_length=100)),
                ('social_facebook', models.CharField(max_length=100)),
                ('social_github', models.CharField(max_length=100)),
                ('social_linkedin', models.CharField(max_length=100)),
                ('social_youtube', models.CharField(max_length=100)),
                ('social_instagram', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'res_company',
            },
        ),
        migrations.CreateModel(
            name='Res_currency',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('rounding', models.FloatField()),
                ('decimal_places', models.IntegerField()),
                ('active', models.BooleanField()),
                ('position', models.CharField(max_length=100)),
                ('currency_unit_label', models.CharField(max_length=100)),
                ('currency_subunit_label', models.CharField(max_length=100)),
                ('create_uid', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('write_uid', models.IntegerField()),
                ('write_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'res_currency',
            },
        ),
        migrations.CreateModel(
            name='Res_partner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company_id', models.IntegerField()),
                ('display_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('title', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('ref', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100)),
                ('tz', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
                ('vat', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('credit_limit', models.FloatField()),
                ('active', models.BooleanField()),
                ('employee', models.BooleanField()),
                ('function', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('street2', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state_id', models.IntegerField()),
                ('country_id', models.IntegerField()),
                ('partner_latitude', models.FloatField()),
                ('partner_longitude', models.FloatField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('is_company', models.BooleanField()),
                ('industry_id', models.IntegerField()),
                ('color', models.IntegerField()),
                ('partner_share', models.BooleanField()),
                ('commenercial_partner_id', models.IntegerField()),
                ('commenercial_company_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('message_main_attachment_id', models.IntegerField()),
                ('email_normalized', models.CharField(max_length=100)),
                ('message_bounce', models.IntegerField()),
                ('signup_token', models.CharField(max_length=100)),
                ('signup_type', models.CharField(max_length=100)),
                ('signup_expiration', models.DateTimeField()),
                ('partner_gid', models.IntegerField()),
                ('additional_info', models.CharField(max_length=100)),
                ('phone_sanitized', models.CharField(max_length=100)),
                ('team_id', models.IntegerField()),
                ('debit_limit', models.FloatField()),
                ('last_time_entries_checked', models.DateTimeField()),
                ('invoice_warn', models.CharField(max_length=100)),
                ('invoice_warn_msg', models.CharField(max_length=100)),
                ('supplier_rank', models.IntegerField()),
                ('customer_rank', models.IntegerField()),
                ('sale_warn', models.CharField(max_length=100)),
                ('sale_warn_msg', models.TextField()),
                ('website_id', models.IntegerField()),
                ('is_published', models.BooleanField()),
                ('create_uid', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('write_uid', models.IntegerField()),
                ('write_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'res_partner',
            },
        ),
        migrations.CreateModel(
            name='Res_users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('company_id', models.IntegerField()),
                ('partner_id', models.IntegerField()),
                ('signature', models.TextField()),
                ('action_id', models.IntegerField()),
                ('share', models.BooleanField()),
                ('alias_id', models.CharField(max_length=100)),
                ('notification_type', models.CharField(max_length=100)),
                ('out_of_office_message', models.CharField(max_length=100)),
                ('sale_team_id', models.IntegerField()),
                ('website_id', models.IntegerField()),
                ('create_uid', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('write_uid', models.IntegerField()),
                ('write_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'res_users',
            },
        ),
    ]
