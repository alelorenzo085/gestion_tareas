# Archivo de manifiesto para el módulo de gestión de tareas en Odoo
{
    'name': 'Gestión de Tareas',
    'version': '1.0',
    'summary': 'Módulo para gestionar tareas individuales de los empleados',
    'category': 'Productivity',
    'author': 'Alejandro Lorenzo',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'hr'],
    'icon': '/gestion_tareas/static/description/icon52.png',
    'data': [
        'views/gestion_tarea_views.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
        Módulo de Odoo para la gestión de tareas asignadas a empleados,
        incluyendo vistas Kanban y formulario detallado.
    """,
}