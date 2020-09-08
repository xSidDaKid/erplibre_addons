# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'ERPLibre package timesheet',
    'version': '12.0.1.0.0',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'timesheet',
    'summary': 'INSTALL ERPLibre package timesheet',
    'description': """
ERPLibre package timesheet
==========================

""",
    'depends': [
        # Custom ERPLibre
        'erplibre_base',

        # addons/Numigi_odoo-timesheet-addons
        'payroll_code_on_task_type',
        'payroll_period',
        'payroll_preparation',
        'payroll_preparation_export_wizard',
        'payroll_preparation_from_timesheet',
        'project_timesheet_time_control_enhanced',
        'timesheet_edit_only_today',
        'timesheet_edit_only_today_grid',
        'timesheet_list_description_after_task',
        'timesheet_list_employee',
        'timesheet_multi_line_wizard',
        'timesheet_multi_line_wizard_grid',
        'timesheet_multi_line_wizard_security',
        'timesheet_payroll_period',
        'timesheet_validation_status',
        'timesheet_validation_status_enterprise',

    ],
    'data': [],
    'installable': True,
}
