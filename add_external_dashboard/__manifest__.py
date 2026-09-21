{
    'name': 'Looker Studio Dashboard',
    'description': 'Dashboard',
    'author': 'Aziz',
    'depends': ['base','web'],
    'application': True,
    'installable': True,
    'version': '1.0',
    'sequence': 1,
    
    'data': [
        'security/ir.model.access.csv',
        'views/looker_studio_input.xml',
        'views/looker_studio_dashboard.xml',
        'views/menuitem.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'looker_studio/static/src/xml/**/*',
            'looker_studio/static/src/js/**/*',
            'looker_studio/static/src/css/**/*',
        ],
    }
}

