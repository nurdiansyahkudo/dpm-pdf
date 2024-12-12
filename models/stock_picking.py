from odoo import models, fields, api

class Picking(models.Model):
    _inherit = "stock.picking"

    total_qty = fields.Integer(string="Total Quantity", compute="_compute_total_qty", store=True)

    @api.depends('move_ids_without_package.quantity')
    def _compute_total_qty(self):
        for picking in self:
            total = sum(line.quantity for line in picking.move_ids_without_package)
            picking.total_qty = total

    def _get_print_report_name(self):
        return 'DPM Delivery Order - %s' % (self.name)

class StockMove(models.Model):
    _inherit = "stock.move"

    line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)
    product_uom_qty = fields.Integer(
        'Demand',
        digits='Product Unit of Measure',
        default=0, required=True,
        help="This is the quantity of product that is planned to be moved."
             "Lowering this quantity does not generate a backorder."
             "Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")
    quantity = fields.Integer(
        'Quantity', compute='_compute_quantity', digits='Product Unit of Measure', inverse='_set_quantity', store=True)

    @api.depends('picking_id')
    def _compute_line_no(self):
        all_pickings = self.mapped('picking_id')
        for picking in all_pickings:
            ordered_moves = picking.move_ids.sorted('id')
            for index, move in enumerate(ordered_moves, start=1):
                move.line_no = index
