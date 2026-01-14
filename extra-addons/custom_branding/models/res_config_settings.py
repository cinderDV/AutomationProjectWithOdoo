from odoo import models, fields, api
import re

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Nombre de empresa
    custom_company_name = fields.Char(
        string='Nombre de Empresa',
        help='Nombre que aparecerá en lugar de "Odoo"',
        config_parameter='custom_branding.company_name',
        default='Mi Empresa',
    )

    # Colores en formato hex
    custom_primary_color = fields.Char(
        string='Color Primario',
        help='Color principal de la interfaz (formato: #RRGGBB)',
        config_parameter='custom_branding.primary_color',
        default='#1E88E5',
    )

    custom_secondary_color = fields.Char(
        string='Color Secundario',
        help='Color secundario de la interfaz (formato: #RRGGBB)',
        config_parameter='custom_branding.secondary_color',
        default='#424242',
    )

    custom_background_color = fields.Char(
        string='Color de Fondo',
        help='Color de fondo del login (formato: #RRGGBB)',
        config_parameter='custom_branding.background_color',
        default='#F5F5F5',
    )

    custom_text_color = fields.Char(
        string='Color de Texto',
        help='Color del texto principal (formato: #RRGGBB)',
        config_parameter='custom_branding.text_color',
        default='#333333',
    )

    @api.constrains('custom_primary_color', 'custom_secondary_color', 'custom_background_color', 'custom_text_color')
    def _check_hex_color_format(self):
        """Valida que los colores estén en formato hexadecimal"""
        hex_pattern = re.compile(r'^#[0-9A-Fa-f]{6}$')

        for record in self:
            colors = {
                'Color Primario': record.custom_primary_color,
                'Color Secundario': record.custom_secondary_color,
                'Color de Fondo': record.custom_background_color,
                'Color de Texto': record.custom_text_color,
            }

            for color_name, color_value in colors.items():
                if color_value and not hex_pattern.match(color_value):
                    raise models.ValidationError(
                        f'{color_name} debe estar en formato hexadecimal (#RRGGBB). '
                        f'Ejemplo: #1E88E5'
                    )
