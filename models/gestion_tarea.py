from odoo import models, fields, api

class GestionTarea(models.Model):
    _name = 'gestion.tarea'
    _description = 'Tarea de Empleado'
    name = fields.Char(string='Nombre de la Tarea', required=True)
    description = fields.Text(string='Descripción')
    assigned_to = fields.Many2one('res.users', string='Usuario Asignado')
    deadline = fields.Date(string='Fecha Límite')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Progreso'),
        ('done', 'Hecho'),
    ], string='Estado', default='draft')
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    ], string='Prioridad', default='1')