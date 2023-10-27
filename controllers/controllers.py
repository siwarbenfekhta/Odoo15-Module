# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request
import json

_logger = logging.getLogger(__name__)


class Eventisi(http.Controller):
    @http.route('/eventisi/eventisi', website="True", auth='public')
    def index(self, **kw):
        event_id = kw.get('event_id')
        event = request.env['eventisi.eventisi'].sudo().search([('id', '=', event_id)])
        if len(event.participants_ids) < event.nb_participant_max:
            return request.render('eventisi.register_form', {'event_id': event_id})

        else:
            html = '<div class="alert alert-warning"" role="status"> Oups ! tickets for this event are sold out<button style="margin-left : 35%" type="button" class="btn btn-danger" disabled>Complet</button></div>'
            return request.render('eventisi.register_success', {'html': html})

    @http.route('/eventisi/create', website="True", auth='public')
    def create_participant(self, **kw):
        html = ''
        event_id = kw.get('event_id')
        event = request.env['eventisi.eventisi'].sudo().search([('id', '=', event_id)])
        #check the existance of participant
        nb_participants = len(request.env['eventisi.participant'].sudo().search([('email' ,'=' , kw.get('email'))]))
        #if participant exists
        if nb_participants > 0:
        #use the existant participant
            participant = request.env['eventisi.participant'].sudo().search([('email' ,'=' , kw.get('email'))])
        else:
		    #else create new participant
            participant_params = {"name": kw.get('name') , "email": kw.get('email'), "phone": kw.get('phone')}
            participant = request.env['eventisi.participant'].sudo().create(participant_params)
        if participant in event.participants_ids:
			#if participant is already registred in event
            html = '<div class="alert alert-danger" role="status">You are already registred </div>'
            return request.render('eventisi.register_success', {'html': html})
        
        request.cr.execute('insert into event_part_rel (name,titre) values(%s,%s)',(participant.id,event.id))
        request.cr.execute('insert into part_event_rel (titre,name) values(%s,%s)',(event.id,participant.id))

        html = '<h1>Thanks !</h1><div class="alert alert-success" role="status"> You are registred successfuly </div> <p>We come back to you shortly !</p>'

        #participant.events_ids = [(kw.get('event_id'), participant.id)]
        #participant = request.env['eventisi.participant'].sudo().save(participant)


        return request.render('eventisi.register_success', {'html': html})
        
		

#     @http.route('/eventisi/eventisi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eventisi.listing', {
#             'root': '/eventisi/eventisi',
#             'objects': http.request.env['eventisi.eventisi'].search([]),
#         })

#     @http.route('/eventisi/eventisi/objects/<model("eventisi.eventisi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eventisi.object', {
#             'object': obj
#         })
