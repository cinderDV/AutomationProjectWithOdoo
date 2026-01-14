from odoo import http
from odoo.http import request
import base64


class CustomBrandingController(http.Controller):

    @http.route('/custom_branding/logo', type='http', auth='public')
    def custom_logo(self, **kwargs):
        """Sirve el logo personalizado desde la configuración"""
        logo_data = request.env['ir.config_parameter'].sudo().get_param('custom_branding.logo')

        if logo_data:
            # Decodificar el logo de base64
            try:
                logo_bytes = base64.b64decode(logo_data)
                return request.make_response(
                    logo_bytes,
                    headers=[
                        ('Content-Type', 'image/png'),
                        ('Cache-Control', 'public, max-age=3600'),
                    ]
                )
            except Exception:
                pass

        # Si no hay logo personalizado, devolver imagen transparente
        transparent_png = base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='
        )
        return request.make_response(
            transparent_png,
            headers=[('Content-Type', 'image/png')]
        )
