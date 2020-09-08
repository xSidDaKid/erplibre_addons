# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package crm',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'crm',
    'summary': 'INSTALL ERPLibre package crm',
    'description': """
ERPLibre package crm
====================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        'crm_filter_all',

        # odoo/addons
        'crm',
        'crm_livechat',
        'crm_phone_validation',
        'crm_project',
        'crm_reveal',

    ],
    'data': [],
    'installable': True,
}
