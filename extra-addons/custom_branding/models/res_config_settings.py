from odoo import models, fields, api
import re
import base64

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Logo personalizado (Binary field - requires manual handling)
    custom_logo = fields.Binary(
        string='Logo Personalizado',
        help='Logo que aparecerá en login y selector de base de datos (recomendado: PNG transparente, 200x50px)',
    )

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

    @api.model
    def get_values(self):
        """Recupera los valores de configuración incluyendo el logo"""
        res = super(ResConfigSettings, self).get_values()
        ICP = self.env['ir.config_parameter'].sudo()

        # Obtener el logo desde ir.config_parameter
        logo_base64 = ICP.get_param('custom_branding.logo', default=False)
        if logo_base64:
            res['custom_logo'] = logo_base64

        return res

    def set_values(self):
        """Guarda los valores de configuración incluyendo el logo"""
        super(ResConfigSettings, self).set_values()
        ICP = self.env['ir.config_parameter'].sudo()

        # Guardar el logo en ir.config_parameter como base64 string
        if self.custom_logo:
            # Si custom_logo ya es base64 string, usar directamente
            # Si es bytes, convertir a base64
            if isinstance(self.custom_logo, bytes):
                logo_base64 = base64.b64encode(self.custom_logo).decode('utf-8')
            else:
                logo_base64 = self.custom_logo

            ICP.set_param('custom_branding.logo', logo_base64)

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
