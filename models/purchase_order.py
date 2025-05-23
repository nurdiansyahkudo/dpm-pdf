from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True, change_default=True, tracking=True, check_company=True, help="You can find a vendor by its Name, TIN, Email or Internal Reference.", domain=[('is_company', '=', True)])

    def get_print_report_name(self):
        return 'DPM Purchase Order - %s' % (self.name)
    def get_print_rfq_name(self):
        return 'DPM Purchase Order - %s' % (self.name)

    @api.depends('order_line.product_qty')
    def _compute_total_qty(self):
        for order in self:
            total = sum(line.product_qty for line in order.order_line)
            order.total_qty = total

class PurchaseOrderLine(models.Model):
  _inherit = "purchase.order.line"

  line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)
  
  @api.depends('order_id')
  def _compute_line_no(self):
      for order in self.mapped('order_id'):
          for index, line in enumerate(order.order_line, start=1):
              line.line_no = index
