from odoo import _, api, fields, models


class DemoModel2Internal(models.Model):
    _name = "aliment.internal"
    _description = "Liste des aliments"

    name = fields.Char()

    # Model_2 contain model_1
    # Only 1 time
    #model_1 = fields.Many2one(comodel_name="demo.model.internal")
