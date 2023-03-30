from odoo import http
from odoo.http import request


class AlimentController(http.Controller):

    @http.route(
        '/listeAliment',
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
        #aliment_names = [a.name for a in aliments]
        aliment_data = [{"id": a.id, "name": a.name} for a in aliments]
        return {"aliments": aliment_data}

    @http.route(
        '/creer_alliment',
        type="json",
        auth="public",
        website=True,
    )
    def ajouterAliment(self, **post):
        http.request.env['aliment.liste'].sudo().create({'name': post.get('name')})


    @http.route(
        '/modifier_aliment',
        type='json',
        auth='public',
        website=True
    )
    def modifier_aliment(self, **post):
        #record = request.env['aliment.liste'].sudo().search([('name', '=', post.get('name'))])
        # record = request.env['aliment.liste'].sudo().search([('id', '=', post.get('id'))])
        # if record:
        #     record.write({'name': post.get('new_name')})
        #     return "Record modified successfully"
        # else:
        #     return "Record not found"
        try:
            record_id = int(post.get('new_id'))
        except ValueError:
            return "Invalid ID value"

        record = request.env['aliment.liste'].sudo().search([('id', '=', record_id)])
        if record:
            record.write({'name': post.get('new_name')})
            return "Record modified successfully"
        else:
            return "Record not found"
