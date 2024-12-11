from odoo import models, fields, api

class Picking(models.Model):
    _inherit = "stock.picking"

    total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)

    @api.depends('move_ids_without_package.quantity')
    def _compute_total_qty(self):
        for picking in self:
            total = sum(line.quantity for line in picking.move_ids_without_package)
            picking.total_qty = total

    def _get_print_report_name(self):
        return 'DPM Delivery Order - %s' % (self.name)
    
class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)

    @api.depends('picking_id')
    def _compute_line_no(self):
        for picking in self.mapped('picking_id'):
            move_lines = picking.move_ids_without_package.mapped('move_id')
            for index, line in enumerate(move_lines, start=1):
                line.line_no = index