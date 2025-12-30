from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_external_order_id = fields.Char(
        string='ID Pedido Externo',
        help='ID del pedido en el marketplace o sistema externo',
        index=True,
    )

    x_delay_status = fields.Selection([
        ('on_time', 'A Tiempo'),
        ('delayed_1_3', 'Retraso 1-3 días'),
        ('delayed_3_plus', 'Retraso +3 días'),
    ], string='Estado Retraso',
       compute='_compute_delay_status',
       store=True,
       help='Estado calculado del retraso del pedido')

    x_delay_days = fields.Integer(
        string='Días de Retraso',
        compute='_compute_delay_days',
        store=True,
        help='Cantidad de días de retraso respecto a fecha compromiso',
    )

    x_stuck_area = fields.Char(
        string='Área de Estancamiento',
        help='Área de fabricación donde está detenido el pedido',
    )

    @api.depends('commitment_date', 'state')
    def _compute_delay_days(self):
        """Calcula los días de retraso basado en la fecha de compromiso"""
        today = fields.Date.today()
        for order in self:
            if order.commitment_date and order.state in ['sale', 'done']:
                delta = (today - order.commitment_date).days
                order.x_delay_days = delta if delta > 0 else 0
            else:
                order.x_delay_days = 0

    @api.depends('x_delay_days')
    def _compute_delay_status(self):
        """Calcula el estado del retraso basado en los días"""
        for order in self:
            if order.x_delay_days == 0:
                order.x_delay_status = 'on_time'
            elif order.x_delay_days <= 3:
                order.x_delay_status = 'delayed_1_3'
            else:
                order.x_delay_status = 'delayed_3_plus'
