# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package purchase',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'purchase',
    'summary': 'INSTALL ERPLibre package purchase',
    'description': """
ERPLibre package purchase
=========================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        # odoo/addons
        'purchase',
        'purchase_mrp',
        'purchase_requisition',
        'purchase_stock',

        # addons/Numigi_odoo-purchase-addons
        'product_supplier_info_helpers',
        'purchase_consignment',
        'purchase_consignment_delivery_expense',
        'purchase_consignment_inventory',
        'purchase_consignment_inventory_line_domain',
        'purchase_estimated_time_arrival',
        'purchase_invoice_empty_lines',
        'purchase_invoice_from_picking',
        'purchase_partner_products',
        'purchase_warning_minimum_amount',

    ],
    'data': [],
    'installable': True,
}
