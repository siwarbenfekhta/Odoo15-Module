from odoo import models, fields, api

import logging


class Praticipant(models.Model):
    _name = 'eventisi.participant'
    _description = 'eventisi.participant'
    _rec_name = "name"
    name = fields.Char('Name')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    events_ids = fields.Many2many(comodel_name='eventisi.eventisi',
                                relation='event_part_rel',
                                column1='name',
                                column2='titre')

