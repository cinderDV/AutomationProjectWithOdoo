{
    'name': 'Custom Branding',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Personalización de marca: logo, colores y textos configurables',
    'description': """
        Módulo de branding personalizado que permite configurar desde Ajustes:
        - Logo personalizado (subir imagen)
        - Nombre de empresa
        - Colores primarios y secundarios (formato hex)
        - Se aplica a pantalla de login y selector de base de datos
    """,
    'author': 'Tu Empresa',
    'website': 'https://www.tufabrica.cl',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_branding/static/src/css/custom_branding.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
