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
    
class StockMove(models.Model):
    _inherit = "stock.move"

    line_no = fields.Integer(string="No.", store=True)

    @api.model
    def create(self, vals):
        if 'line_no' not in vals:
            existing_lines = self.search([('picking_id', '=', vals.get('picking_id'))])
            vals['line_no'] = len(existing_lines) + 1
        return super(StockMove, self).create(vals)