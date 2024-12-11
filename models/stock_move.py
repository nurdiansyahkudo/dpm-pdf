from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = "stock.move"

    line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)

    @api.depends('move_line_ids')
    def _compute_line_no(self):
        for move in self:
            # Enumerate over move.move_line_ids to assign sequential line_no
            for index, line in enumerate(move.move_line_ids, start=1):
                line.line_no = index

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    line_no = fields.Integer(string="No.")
