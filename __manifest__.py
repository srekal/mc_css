# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'mc_css',
    'version': '1.0',
    'summary': '添加自定义样式',
    'description': """
    修改 static/src/css/style.css进行样式变更

 """,
    'depends': ['base'],
    'data': [

        'views/style.xml',

    ],
    'installable': True,
    'auto_install': False,
}
