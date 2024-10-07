from odoo import models, fields, api
from datetime import timedelta
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    product_id = fields.Many2one('sale.order.line', string='Product', required=True)
    
    warranty_period = fields.Integer(related='product_id.warranty_period', string='Warranty Period', store=True, readonly=False)
    
    order_date = fields.Date(string='Order Date', default=fields.Date.today, required=True)

    warranty_expiry_date = fields.Date(string='Warranty Expiry Date', compute='_compute_warranty_expiry', store=True)

    @api.depends('order_date', 'warranty_period')
    def _compute_warranty_expiry(self):
        for record in self:
            if record.warranty_period and record.order_date:
                record.warranty_expiry_date = record.order_date + timedelta(days=record.warranty_period)
            else:
                record.warranty_expiry_date = False

    @api.model
    def send_warranty_notifications(self):
        today = fields.Date.today()
        soon_expiring = self.search([
            ('warranty_expiry_date', '>', today),
            ('warranty_expiry_date', '<=', today + timedelta(days=30)),
            ('state', '=', 'posted')  # Ensure the invoice is posted
        ])
        _logger.info(f"Found {len(soon_expiring)} invoices expiring soon.")
        for invoice in soon_expiring:
            _logger.info(f"Sending email for {invoice.id} to {invoice.partner_id.email}")
            template_id = self.env.ref('new_task.mail_template_warranty_expiry', raise_if_not_found=False)
            if template_id:
                template_id.send_mail(invoice.id, force_send=True)
            else:
                _logger.warning("Warranty expiry notification template not found.")

