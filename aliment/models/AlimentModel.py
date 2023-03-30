from odoo import _, fields, models, api


class AlimentModel(models.Model):
    _name = 'aliment.liste'
    _description = 'Liste des aliments'

    id = fields.Integer(string='ID', required=True, readonly=True, index=True, default=1)
    name = fields.Char(string='Name')
