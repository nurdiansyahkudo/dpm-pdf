from odoo import models, fields, api
from datetime import datetime

class AccountMove(models.Model):
      _inherit = "account.move"

      custom_invoice_date = fields.Date(
            string="Custom Invoice Date", 
            readonly=True, 
            store=True, 
            compute="_compute_custom_invoice_date_from_origin", 
            help="The invoice date from the related invoice reference."
      )

      @api.depends('ref')
      def _compute_custom_invoice_date_from_origin(self):
            for record in self:
                  if record.ref:
                        related_invoice = self.env['account.move'].search([('name', '=', record.ref)], limit=1)
                        if related_invoice:
                              record.custom_invoice_date = related_invoice.invoice_date

      def get_print_report_name(self):
            return 'DPM Supplier Invoice - %s' % (self.name)
      
      def get_payment_voucher_print_report_name(self):
            return 'DPM Payment Voucher - %s' % (self.name)
      
      def get_receipt_voucher_print_report_name(self):
            return 'DPM Receipt Voucher - %s' % (self.name)
  