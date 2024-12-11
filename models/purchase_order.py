from odoo import models, fields, api

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"

  line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)

  def get_print_report_name(self):
        return 'DPM Purchase Order - %s' % (self.name)
  
  @api.depends('order_id')
  def _compute_line_no(self):
      for order in self.mapped('order_id'):
          for index, line in enumerate(order.order_line, start=1):
              line.line_no = index
  