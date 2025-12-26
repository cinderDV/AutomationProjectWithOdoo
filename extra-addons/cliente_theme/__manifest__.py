# -*- coding: utf-8 -*-
{
    'name': 'Cliente - Tema Personalizado',
    'version': '18.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Personalización de UI/UX - Branding y Assets',
    'description': '''
        Módulo de personalización completo para Odoo 18.0
        ================================================

        **Nivel 1 - Assets (Branding Visual)**
        - Variables SCSS personalizadas (colores, fuentes)
        - Logo personalizado en navbar
        - Favicon personalizado
        - Fondo de pantalla de login

        **Nivel 2 - Estructura (Vistas XML)**
        - Modificación del navbar (web.layout)
        - Personalización de la pantalla de login
        - Ajustes de formularios y vistas

        Desarrollado para entorno Docker + Coolify
    ''',
    'author': 'Tu Empresa',
    'website': 'https://tuempresa.com',
    'license': 'LGPL-3',
    'depends': [
        'web',
        # 'web_enterprise',  # Descomentar si usas Enterprise
    ],
    'data': [
        # Panel de configuración
        'views/res_config_settings_views.xml',
        # Vistas XML del backend
        'views/webclient_templates.xml',
        'views/login_templates.xml',
    ],
    'assets': {
        # Assets del Backend
        'web.assets_backend': [
            'cliente_theme/static/src/scss/custom_theme.scss',
        ],
        # Assets del Frontend (Portal/Website si lo usas)
        'web.assets_frontend': [
            'cliente_theme/static/src/scss/custom_theme.scss',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
