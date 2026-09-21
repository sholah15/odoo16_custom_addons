{
        'name': "PostgreSQL Query Deluxe - Googlesheets",

        'summary': """
            Execute postgreSQL query into Googlesheets
        """,

        'description': """
            Execute postgreSQL query into Googlesheets
        """,

        'author': "Aziz",
        'website': "https://cerindocorp.com/",
        'images': [],
        'category': 'cerindocorp',
        "application": True,
        "installable": True,
        'version': '1.0',
        'sequence': 0,

        # any module necessary for this one to work correctly
        'depends': ['base', 'mail', 'query_deluxe'],

        # always loaded
        'data': [
            'security/ir.model.access.csv',
            'views/menu.xml',
            'views/query_deluxe_googlesheet.xml',
            'views/credentials.xml',
            'data/update_spreadsheets.xml',
            ],
        
}

