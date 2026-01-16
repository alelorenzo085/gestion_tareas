{
    'name': 'Gestión de Tareas',
    'version': '1.0',
    'summary': 'Módulo para gestionar tareas individuales de los empleados',
    'category': 'Productivity',
    'author': 'David Márquez',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'icon': '/gestion_tareas/static/description/icon52.png',
    'data': [
        'views/gestion_tarea_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/gestion_tareas/static/src/css/styles.css',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
        Módulo de Odoo para la gestión de tareas asignados a empleados,
        incluyendo vistas Kanban y formulario detallado.
    """,
}