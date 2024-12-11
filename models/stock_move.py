from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    line_no = fields.Integer(string="No.", compute="_compute_line_no", store=True)

    @api.depends('move_id.move_line_ids')
    def _compute_line_no(self):
        for move in self.mapped('move_id'):
            for index, line in enumerate(move.move_line_ids, start=1):
                line.line_no = index
