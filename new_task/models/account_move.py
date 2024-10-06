from odoo import models, fields, api
from datetime import timedelta
class AccountMove(models.Model):
    _inherit = 'account.move'

    product_id = fields.Many2one('sale.order.line', string='Product', required=True)
    
    warranty_period = fields.Integer(related='product_id.warranty_period', string='Warranty Period', store=True, readonly=False)
    
    order_date = fields.Date(string='Order Date', default=fields.Date.today, required=True)

    warranty_expiry_date = fields.Date(string='Warranty Expiry Date', compute='_compute_warranty_expiry', store=True)

    @api.depends('order_date', 'warranty_period')
    def _compute_warranty_expiry(self):
        for record in self:
            if record.warranty_period == 0:
                record.warranty_expiry_date = record.order_date
            else:
                if record.order_date and record.warranty_period:
                    record.warranty_expiry_date = fields.Date.add(record.order_date, days=record.warranty_period)
                else:
                    record.warranty_expiry_date = False

