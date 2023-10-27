from odoo import models, fields, api


class lieu(models.Model):
    _name = 'eventisi.lieu'
    _description = 'eventisi.lieu'
    _rec_name = 'address'
    address = fields.Char('Adresse')
