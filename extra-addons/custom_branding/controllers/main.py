from odoo import http
from odoo.http import request
import base64


class CustomBrandingController(http.Controller):

    @http.route('/custom_branding/logo', type='http', auth='public')
    def custom_logo(self, **kwargs):
        """Sirve el logo desde la configuración de la compañía principal"""
        try:
            # Obtener el logo de la compañía principal
            company = request.env['res.company'].sudo().search([], limit=1)

            if company and company.logo:
                # El logo ya está en base64
                logo_bytes = base64.b64decode(company.logo)
                return request.make_response(
                    logo_bytes,
                    headers=[
                        ('Content-Type', 'image/png'),
                        ('Cache-Control', 'public, max-age=3600'),
                    ]
                )
        except Exception:
            pass

        # Si no hay logo, devolver imagen transparente
        transparent_png = base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='
        )
        return request.make_response(
            transparent_png,
            headers=[('Content-Type', 'image/png')]
        )
