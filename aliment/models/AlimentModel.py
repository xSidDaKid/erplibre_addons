from odoo import _, fields, models, api


class AlimentModel(models.Model):
    _name = 'aliment.liste'
    _description = 'Liste des aliments'

    name = fields.Char(strings)
