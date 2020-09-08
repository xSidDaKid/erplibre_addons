# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package business-requirement',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'stock',
    'summary': 'INSTALL ERPLibre package business-requirement',
    'description': """
ERPLibre package business-requirement
=====================================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        # addons/OCA_business-requirement
        'business_requirement',
        'business_requirement_crm',
        'business_requirement_deliverable',
        'business_requirement_sale',
        'business_requirement_sale_timesheet',

    ],
    'data': [],
    'installable': True,
}
