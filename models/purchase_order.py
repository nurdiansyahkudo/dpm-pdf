from odoo import models

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"

  def get_print_report_name(self):
        return 'DPM Purchase Order - %s' % (self.name)