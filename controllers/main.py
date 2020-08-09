
# -*- coding: utf-8 -*-

import logging

from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleGuadalstoreProductInfo(WebsiteSale):

    @http.route()
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        """ Added ref and barcode to original response """
        res = super(WebsiteSaleGuadalstoreProductInfo, self).get_combination_info_website(product_template_id, product_id, combination, add_qty, **kw)
        product = request.env['product.product'].browse(res['product_id'])
        res.update({
            'before_product_id': product_id,
            'brand_name': request.env['product.template'].browse(res['product_template_id']).product_brand_id.name,
            'barcode': product.barcode,
            'default_code': product.default_code
        })

        return res
