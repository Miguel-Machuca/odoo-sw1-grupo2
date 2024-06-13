{
    'name': 'Profesor Management',
    'version': '1.0',
    'summary': 'Manage Profesor Records',
    'description': """
        A module to manage profesor records including their details and courses they teach.
    """,
    'author': 'Your Name',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/profesor_views.xml',
    ],
    'installable': True,
    'application': True,
}
