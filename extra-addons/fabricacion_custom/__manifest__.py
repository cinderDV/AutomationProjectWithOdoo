{
    'name': 'Fabricación Custom',
    'version': '18.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'Campos personalizados para gestión de fabricación de muebles',
    'description': """
        Módulo custom que agrega:
        - SKUs de marketplaces en productos
        - Canal de venta en clientes
        - Campos de seguimiento de retrasos en pedidos
        - Gestión avanzada de merma y devoluciones
    """,
    'author': 'Tu Empresa',
    'website': 'https://www.tufabrica.cl',
    'depends': [
        'base',
        'product',
        'sale',
        'stock',
        'mrp',
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_scrap_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
