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

    @http.route(
        '/delete_aliment',
        type='json',
        auth="user",
        website=True
    )
    def delete_record(self, **kw):
        try:
            record_id = int(kw.get('old_id'))
        except ValueError:
            return "Invalid ID value"
        record = request.env['aliment.liste'].sudo().search([('id', '=', record_id)])
        if record:
            record.unlink()
            return request.redirect('/')
        else:
            return request.render('aliment.liste.error', {'message': 'Record not found'})