from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = "stock.move"

    move_line_ids = fields.One2many('stock.move.line', 'move_id', string="Move Lines")
    
    @api.depends('move_line_ids')
    def _compute_line_no(self):
        for move in self:
            for index, line in enumerate(move.move_line_ids, start=1):
                line.line_no = index

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    line_no = fields.Integer(string="No.")
