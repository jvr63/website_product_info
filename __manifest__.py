# -*- coding: utf-8 -*-
{
    'name': "Show advanced product info",
    'summary': 'Show template info into product',
    'description': """
Show more info into template website_sale.product as EAN/REF, etc
    """,
    'author': 'Juan Vázquez Moreno',
    'category': 'Website',
    'version': '1.0',
    'depends': ['website_sale'],
    'data': [
        'views/website_sale_template_info.xml'
    ],
    'installable': True,
}
