from odoo import http
from odoo.http import request


class AlimentController(http.Controller):

    @http.route(
        '/creer_alliment',
        type="http",
        auth="public",
        website=True,
    )
    def creerAliment(self, **post):
        aliment = request.env['liste.aliment'].create({'name' : post.get('name')})

    @http.route(
        '/get_all',
        type="http",
        auth="public",
        website=True,
    )
    def creerAliment(self, **post):
        unAliment = http.request.env['aliment.liste']
        aliment_ids = unAliment.search([])
        items = unAliment.browse(aliment_ids)
        return http.request.render('my_module.item_list_template', {'items': items})


