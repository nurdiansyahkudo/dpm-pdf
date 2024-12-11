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
      total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)

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
      
      @api.depends('invoice_line_ids.quantity')
      def _compute_total_qty(self):
            for move in self:
                  total = sum(line.quantity for line in move.invoice_line_ids)
                  move.total_qty = total

class AccountMoveLine(models.Model):
  _inherit = "account.move.line"

  line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)
  
  @api.depends('move_id')
  def _compute_line_no(self):
      for move in self.mapped('move_id'):
          for index, line in enumerate(move.invoice_line_ids, start=1):
              line.line_no = index