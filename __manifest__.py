{
    'name': "Show advanced product info",
    'summary': 'Show more product info',
    'description': """
Show more info into template website_sale.product as EAN/REF, etc
    """,
    'author': 'Juan Vázquez Moreno',
    'category': 'Website',
    'version': '1.0',
    'depends': ['website_search'],
    'data': [
        'views/website_sale_template_info.xml',
        'views/website_sale_product_info.xml',
        'views/website_sale_template_produts_description.xml',
    ],
    'installable': True,
}
