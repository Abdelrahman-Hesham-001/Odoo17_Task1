{
    'name': 'ToDo',
    'version': '1.0',
    'category': "",
    'author': 'Abdelrahman Hesham',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu_view.xml',
        'views/todo_views.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'todo_app/static/src/css/todo.css'
        ]
    },
    'installable': True,
    'application': True,
}
