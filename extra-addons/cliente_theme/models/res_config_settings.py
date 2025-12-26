# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """
    Configuraciones personalizadas del tema
    Permite subir logo, favicon y personalizar colores desde la interfaz
    """
    _inherit = 'res.config.settings'

    # ==================================================================
    # CAMPOS DE PERSONALIZACIÓN DE IMÁGENES
    # ==================================================================

    theme_backend_logo = fields.Binary(
        string='Logo del Backend (Navbar)',
        help='Logo que aparece en la barra superior del backend. '
             'Tamaño recomendado: 200x60 px (PNG transparente)',
        config_parameter='cliente_theme.backend_logo'
    )

    theme_favicon = fields.Binary(
        string='Favicon',
        help='Icono que aparece en la pestaña del navegador. '
             'Tamaño: 16x16 o 32x32 px (ICO o PNG)',
        config_parameter='cliente_theme.favicon'
    )

    theme_login_background = fields.Binary(
        string='Fondo de Pantalla de Login',
        help='Imagen de fondo para la pantalla de login. '
             'Tamaño recomendado: 1920x1080 px (JPG)',
        config_parameter='cliente_theme.login_background'
    )

    # ==================================================================
    # CAMPOS DE PERSONALIZACIÓN DE COLORES
    # ==================================================================

    theme_primary_color = fields.Char(
        string='Color Primario',
        help='Color principal del tema (ej: #1E40AF)',
        default='#1E40AF',
        config_parameter='cliente_theme.primary_color'
    )

    theme_secondary_color = fields.Char(
        string='Color Secundario',
        help='Color secundario del tema (ej: #10B981)',
        default='#10B981',
        config_parameter='cliente_theme.secondary_color'
    )

    # ==================================================================
    # CAMPOS DE PERSONALIZACIÓN DE TEXTOS
    # ==================================================================

    theme_company_name = fields.Char(
        string='Nombre de la Empresa (Navbar)',
        help='Texto que aparece junto al logo en el navbar',
        default='Mi Empresa',
        config_parameter='cliente_theme.company_name'
    )

    theme_login_title = fields.Char(
        string='Título de Login',
        help='Título que aparece en la pantalla de login',
        default='Bienvenido al ERP',
        config_parameter='cliente_theme.login_title'
    )

    theme_login_subtitle = fields.Char(
        string='Subtítulo de Login',
        help='Subtítulo debajo del título de login',
        default='Inicia sesión para continuar',
        config_parameter='cliente_theme.login_subtitle'
    )

    theme_page_title = fields.Char(
        string='Título de la Página',
        help='Título que aparece en la pestaña del navegador',
        default='Cliente ERP - Odoo',
        config_parameter='cliente_theme.page_title'
    )

    # ==================================================================
    # CAMPOS DE PERSONALIZACIÓN DE FOOTER
    # ==================================================================

    theme_footer_text = fields.Char(
        string='Texto del Footer',
        help='Texto que aparece en el pie de página del backend',
        default='© 2025 Tu Empresa - Powered by Odoo 18.0',
        config_parameter='cliente_theme.footer_text'
    )
