# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Odoo Tutorial""",

    'description': """
        This is a tutorial for using odoo to build a management software for
        open course.
    """,

    'author': "Justin Zhu",
    'website': "http://www.polarwin.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'tutorial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        #'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
