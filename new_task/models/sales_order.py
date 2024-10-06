from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty_period = fields.Integer(string="Warranty Period", help="Warranty period in days.")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.warranty_period = self.product_id.warranty_period


class WarrantyReport(models.Model):
    _name = 'warranty.report'
    _description = 'Warranty Report'

    order = fields.Char(string='Sale Order', default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Customer', store=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    
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
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['order'] = self.env['ir.sequence'].next_by_code('warranty.report.order') or _('New')
        return super(WarrantyReport, self).create(vals_list)
