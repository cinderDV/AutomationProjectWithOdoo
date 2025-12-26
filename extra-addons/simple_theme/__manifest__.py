# -*- coding: utf-8 -*-
{
    'name': 'Simple Backend Theme',
    'version': '18.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Tema simple y funcional para personalizar Odoo - SIN dependencias externas',
    'description': '''
        Tema Simple para Odoo 18.0
        ==========================

        ✅ Sin dependencias externas (solo requiere 'web')
        ✅ Panel de configuración visual
        ✅ Sube logo, favicon, y fondo de login desde la interfaz
        ✅ Selector de colores corporativos
        ✅ Textos personalizables

        **Configuración:**
        Ajustes > General Settings > Simple Theme
    ''',
    'author': 'Tu Empresa',
    'website': 'https://tuempresa.com',
    'license': 'LGPL-3',
    'depends': [
        'web',  # Solo depende de 'web' que viene por defecto
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/webclient_templates.xml',
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'simple_theme/static/src/scss/backend_theme.scss',
        ],
        'web.assets_frontend': [
            'simple_theme/static/src/scss/backend_theme.scss',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
