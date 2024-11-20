from odoo import models

class SaleOrder(models.Model):
  _inherit = "sale.order"

  def get_print_report_name(self):
        return 'DPM Sales Order - %s' % (self.name)