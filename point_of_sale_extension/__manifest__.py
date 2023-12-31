# -*- coding: utf-8 -*-
{
    'name': "point_of_sale_extension",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'views/templates.xml',
        'views/view.xml',
    ],
    'assets': {
       'point_of_sale.assets': [
           'point_of_sale_extension/static/src/js/*.js',
       ],
    'web.assets_qweb': [
            'point_of_sale_extension/static/src/xml/**/*',
        ],
    },
    'qweb': ['point_of_sale_extension/static/src/xml/*.xml'],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
