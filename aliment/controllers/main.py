from odoo import http
from odoo.http import request


class AlimentController(http.Controller):

    @http.route(
        ['/listeAliment'],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def getAllAliment(self):
        #aliments = request.env['aliment.liste'].sudo().search([])
        aliments = [
            {'name': 'Aliment 1'},
            {'name': 'Aliment 2'},
            {'name': 'Aliment 3'},
        ]
        #return request.render('aliment.s_aliment', {'aliments': aliments})
        return {"aliments":["viande", "legume","fruit"]}

    @http.route(
        '/creer_alliment',
        type="http",
        auth="public",
        website=True,
    )
    def ajouterAliment(self, **post):
        http.request.env['aliment.liste'].sudo().create({'name': post.get('name')})

