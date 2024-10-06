from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class ProductProduct(models.Model):
    _inherit = 'product.product'

    warranty_period = fields.Integer(string='Warranty Period')
    manufacturer = fields.Many2one('res.partner', string="Manufacturer")




