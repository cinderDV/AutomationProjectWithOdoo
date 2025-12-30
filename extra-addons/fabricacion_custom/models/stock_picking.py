from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    x_return_process = fields.Selection([
        ('solo_almacenar', 'Solo Almacenar'),
        ('reparar', 'Reparar'),
        ('desechar', 'Desechar'),
        ('reemplazar', 'Reemplazar'),
    ], string='Proceso a Seguir',
       help='Acción a realizar con el producto devuelto')

    x_responsible_worker_id = fields.Many2one(
        'hr.employee',
        string='Trabajador Responsable',
        help='Empleado responsable de gestionar la devolución',
    )
