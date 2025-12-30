from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_sales_channel = fields.Selection([
        ('marketplace_falabella', 'Falabella'),
        ('marketplace_ripley', 'Ripley'),
        ('marketplace_paris', 'Paris'),
        ('ecommerce_propio', 'Ecommerce Propio'),
        ('persona_natural', 'Persona Natural'),
        ('empresa_directa', 'Empresa Directa'),
        ('vendedor_directo', 'Vendedor Directo'),
        ('otro', 'Otro'),
    ], string='Canal de Venta',
       help='Canal de origen del cliente',
       index=True)
