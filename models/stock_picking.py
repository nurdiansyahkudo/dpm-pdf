from odoo import models, fields, api

class Picking(models.Model):
  _inherit = "stock.picking"

  total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)

  def _get_print_report_name(self):
    return 'DPM Delivery Order - %s' % (self.name)
  
  @api.depends('move_ids_without_package.quantity')
  def _compute_total_qty(self):
      for move in self:
          total = sum(line.quantity for line in move.move_ids_without_package)
          move.total_qty = total

class StockMoveLine(models.Model):
  _inherit = "stock.move.line"

  line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)
  
  @api.depends('move_id')
  def _compute_line_no(self):
      for move in self.mapped('move_id'):
          for index, line in enumerate(move.move_ids_without_package, start=1):
              line.line_no = index