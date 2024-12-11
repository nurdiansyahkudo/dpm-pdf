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