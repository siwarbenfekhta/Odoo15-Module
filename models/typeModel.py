from odoo import models, fields, api


class Type(models.Model):
    _name = 'eventisi.type'
    _description = 'eventisi.type'
    _rec_name = 'label'
    label = fields.Char('Label')
