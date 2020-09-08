# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package property management',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'property management',
    'summary': 'INSTALL ERPLibre package property management',
    'description': """
ERPLibre package property management
====================================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        # addons/dhongu_deltatech
        'deltatech_property',
        'deltatech_property_agreement',
    ],
    'data': [],
    'installable': True,
}
