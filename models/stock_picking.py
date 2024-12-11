from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    line_no = fields.Integer(string="No.")

class Picking(models.Model):
    _inherit = "stock.picking"

    total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)
    
    @api.depends('move_ids_without_package')
    def _compute_line_no(self):
        for picking in self:
            for index, line in enumerate(picking.move_ids_without_package, start=1):
                line.line_no = index

    @api.depends('move_ids_without_package.quantity')
    def _compute_total_qty(self):
        for picking in self:
            total = sum(line.quantity for line in picking.move_ids_without_package)
            picking.total_qty = total

    def _get_print_report_name(self):
        return 'DPM Delivery Order - %s' % (self.name)
