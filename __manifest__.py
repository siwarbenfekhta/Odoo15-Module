# -*- coding: utf-8 -*-
{
    'name': "Eventisi",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'sequence' : "-1000",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing/Events',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'mail'],

    # always loaded
    'data': [
        'views/event_view.xml',
        'views/type_views.xml',
        'views/lieu_views.xml',
        'reports/report.xml',
        'reports/badge.xml',
        'views/registration_views.xml',
        'views/list_participant_views.xml',
        'views/reg_success_views.xml',
        'views/reporting_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'eventisi/static/src/scss/event.scss',
            'event/static/src/js/field_icon_selection.js',
        ],
        'web.assets_common': [
            'eventisi/static/src/js/tours/**/*',
        ],
        'web.assets_qweb': [
            'eventisi/static/src/xml/**/*',
        ],
        'web.report_assets_common': [
            '/eventisi/static/src/scss/event_foldable_badge_report.scss',
            '/eventisi/static/src/scss/event_full_page_ticket_report.scss',
            '/eventisi/static/src/scss/event.css'
        ],
        'web.report_assets_pdf': [
            '/eventisi/static/src/scss/event_full_page_ticket_report_pdf.scss',
            '/eventisi/static/src/scss/event.css'
        ],
    },

}
