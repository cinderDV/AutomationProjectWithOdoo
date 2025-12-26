# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Imágenes
    simple_theme_logo = fields.Binary(
        string='Logo del Backend',
        help='Logo de la barra superior (200x60 px)',
        config_parameter='simple_theme.logo'
    )

    simple_theme_favicon = fields.Binary(
        string='Favicon',
        help='Icono de la pestaña (16x16 px)',
        config_parameter='simple_theme.favicon'
    )

    simple_theme_login_bg = fields.Binary(
        string='Fondo de Login',
        help='Imagen de fondo (1920x1080 px)',
        config_parameter='simple_theme.login_bg'
    )

    # Colores
    simple_theme_primary = fields.Char(
        string='Color Primario',
        default='#1E40AF',
        config_parameter='simple_theme.primary'
    )

    simple_theme_secondary = fields.Char(
        string='Color Secundario',
        default='#10B981',
        config_parameter='simple_theme.secondary'
    )

    # Textos
    simple_theme_company_name = fields.Char(
        string='Nombre de Empresa',
        default='Mi Empresa',
        config_parameter='simple_theme.company_name'
    )

    simple_theme_page_title = fields.Char(
        string='Título de Página',
        default='ERP - Odoo',
        config_parameter='simple_theme.page_title'
    )
