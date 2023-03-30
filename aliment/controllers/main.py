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
        aliments = request.env['aliment.liste'].sudo().search([])
        #return request.render('aliment.s_aliment', {'aliments': aliments})
        #return {"aliments":["viande", "legume","fruit"]}
        aliment_names = [a.name for a in aliments]
        return {"aliments": aliment_names}

    @http.route(
        '/creer_alliment',
        type="json",
        auth="public",
        website=True,
    )
    def ajouterAliment(self, **post):
        http.request.env['aliment.liste'].sudo().create({'name': post.get('name')})

