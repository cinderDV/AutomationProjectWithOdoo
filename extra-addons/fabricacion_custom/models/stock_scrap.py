from odoo import models, fields

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    x_incident_type = fields.Selection([
        ('error_humano', 'Error Humano'),
        ('material_defectuoso', 'Material Defectuoso'),
        ('diseno_defectuoso', 'Diseño Defectuoso'),
        ('accidente', 'Accidente'),
        ('otro', 'Otro'),
    ], string='Tipo de Incidente',
       help='Clasificación del tipo de error que causó la merma',
       required=False)

    x_economic_impact = fields.Float(
        string='Impacto Económico (CLP)',
        digits=(16, 2),
        help='Costo económico de la merma en pesos chilenos',
    )

    x_action_taken = fields.Selection([
        ('desechar', 'Desechar'),
        ('reutilizar', 'Reutilizar'),
        ('reparar', 'Reparar'),
        ('investigar', 'Investigar'),
    ], string='Acción Tomada',
       help='Acción realizada con el material defectuoso')

    x_area_occurrence = fields.Char(
        string='Área de Ocurrencia',
        help='Área de fabricación donde ocurrió el incidente',
    )
