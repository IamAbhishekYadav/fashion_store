# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fashion Store',
    'version': '0.1',
    'summary': 'Simple Fashion store functions',
    'description': """This module is for training purpose on Fashion tore
    """,
    'depends': ['base'],
    'data': [

        'views/FashionGarment.xml',
        'views/Order.xml',
        'views/OrderLine.xml',
    ],
    'installable': True,
    'auto_install': False
}