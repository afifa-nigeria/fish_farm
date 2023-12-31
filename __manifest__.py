{
    'name': 'Fish Farm',
    'version': '1.0',
    'summary': 'Custom module for fish farming',
    'description': 'This module manages fish farming operations.',
    'category': 'Custom',
    'author': 'Dr. Aminu Abubakar',
    'website': 'https://afifa.ng',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/fish_stock_intake_views.xml',
        'views/pond_views.xml',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
