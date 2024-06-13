from odoo import models, fields

class Profesor(models.Model):
    _name = 'profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad')
    subject = fields.Char(string='Asignatura')
    email = fields.Char(string='Email')
