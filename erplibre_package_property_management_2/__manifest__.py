# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package property management 2',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'property management 2',
    'summary': 'INSTALL ERPLibre package property management 2',
    'description': """
ERPLibre package property management 2
======================================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        # addons/kinjal-sorathiya_Property-Management_odoo
        'cr_property',
    ],
    'data': [],
    'installable': True,
}
