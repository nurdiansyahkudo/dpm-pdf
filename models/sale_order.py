from odoo import models, fields, api

class SaleOrder(models.Model):
  _inherit = "sale.order"

  total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)
  total_qty_delivered = fields.Float(string="Total Quantity Delivered", compute="_compute_total_qty_delivered", store=True)

  def get_print_report_name(self):
      return 'DPM Sales Order - %s' % (self.name)
  
  @api.depends('order_line.product_uom_qty')
  def _compute_total_qty(self):
      for order in self:
          total = sum(line.product_uom_qty for line in order.order_line)
          order.total_qty = total

  @api.depends('order_line.qty_delivered')
  def _compute_total_qty(self):
      for order in self:
          total = sum(line.qty_delivered for line in order.order_line)
          order.total_qty_delivered = total

class SaleOrderLine(models.Model):
  _inherit = "sale.order.line"

  line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)
  
  @api.depends('order_id')
  def _compute_line_no(self):
      for order in self.mapped('order_id'):
          for index, line in enumerate(order.order_line, start=1):
              line.line_no = index