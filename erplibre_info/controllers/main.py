from odoo import http
from odoo.addons.web_settings_dashboard.controllers.main import WebSettingsDashboard
import subprocess

class WebSettingsDashboardERPLibre(WebSettingsDashboard):

    @http.route('/web_settings_dashboard/data', type='json', auth='user')
    def web_settings_dashboard_data(self, **kw):
        res = super(WebSettingsDashboardERPLibre, self).web_settings_dashboard_data()
        if res:
            share = res.get("share")
            if share:
                # share["server_erplibre_version"] = "10294"
                share["server_erplibre_commit"] = subprocess.check_output(["git", "describe", "--tags"]).strip()
        return res
