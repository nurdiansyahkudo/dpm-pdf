# -*- coding: utf-8 -*-
{
    'name': "DPM Custom Report ",
    'summary': '',
    'author': 'Rizky Abdi',
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'purchase', 'sale', 'account', 'stock'],
    'data': [
        'report/dpm_vendor_bill_report.xml',
        'views/dpm_vendor_bill_template.xml',
        'report/dpm_purchase_order_report.xml',
        'views/dpm_purchase_order_template.xml',
        'report/dpm_sales_order_report.xml',
        'views/dpm_sales_order_template.xml',
        'report/dpm_delivery_order_report.xml',
        'views/dpm_delivery_order_template.xml',
        'report/dpm_good_receipt_report.xml',
        'views/dpm_good_receipt_template.xml',
        'report/dpm_payment_voucher_report.xml',
        'views/dpm_payment_voucher_template.xml',
        'report/dpm_receipt_voucher_report.xml',
        'views/dpm_receipt_voucher_template.xml',
        'views/voucher_view.xml',
    ],
    'installable': True,
    'application': False,
}

