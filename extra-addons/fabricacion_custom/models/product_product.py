from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    x_sku_falabella = fields.Char(
        string='SKU Falabella',
        help='SKU del producto en Falabella Marketplace',
        index=True,
    )

    x_sku_ripley = fields.Char(
        string='SKU Ripley',
        help='SKU del producto en Ripley Marketplace',
        index=True,
    )

    x_sku_paris = fields.Char(
        string='SKU Paris',
        help='SKU del producto en Paris Marketplace',
        index=True,
    )
