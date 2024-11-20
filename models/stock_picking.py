from odoo import models

class Picking(models.Model):
  _inherit = "stock.picking"

  def _get_print_report_name(self):
    return 'DPM Delivery Order - %s' % (self.name)