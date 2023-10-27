from odoo import models, fields, api

import logging


class eventisi(models.Model):
    _name = 'eventisi.eventisi'
    _description = 'eventisi.eventisi'
    _rec_name = "titre"
    _inherit = 'mail.thread'
    titre = fields.Char()
    date = fields.Date('Date')
    duree = fields.Integer('Duree')
    url = fields.Char('URL', compute="set_url")
    nb_participant_max = fields.Integer('Nb participant max')
    nb_participant_reste = fields.Char('NB Participant restant', compute="set_nb_participant")
    nb_inscris = fields.Char('NB inscris', compute="set_nb_inscris")
    type_id = fields.Many2one(comodel_name='eventisi.type', string='Type')
    lieu_id = fields.Many2one(comodel_name='eventisi.lieu', string='Lieu')
    organizer_id = fields.Many2one(
        'res.partner', string='Organizer', tracking=True,
    )
    participants_ids = fields.Many2many(comodel_name='eventisi.participant',
                                relation='part_event_rel',
                                column1='titre',
                                column2='name')
    
    @api.depends("url")
    def set_url(self):
        self.url = 'http://localhost:8069/eventisi/eventisi?event_id='+str(self.id)
      
    @api.depends("nb_participant_reste")
    def set_nb_participant(self):
        self.nb_participant_reste = self.nb_participant_max - len(self.participants_ids)

    @api.depends("nb_inscris")
    def set_nb_inscris(self):
        self.nb_inscris = len(self.participants_ids)

    @api.depends("url")
    def website_go_to(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/eventisi/eventisi?event_id='+str(self.id),
            'target': 'new',
        }
        


