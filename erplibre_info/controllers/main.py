from odoo import http
from odoo.addons.web_settings_dashboard.controllers.main import WebSettingsDashboard
import subprocess
import pexpect


def cmdlineCall(name, args):
    child = pexpect.spawn(name, args)
    # Wait for the end of the output
    child.expect(pexpect.EOF)
    out = child.before  # we get all the data before the EOF (stderr and stdout)
    child.close()  # that will set the return code for us
    # signalstatus and existstatus read as the same (for my purpose only)
    if child.exitstatus is None:
        returncode = child.signalstatus
    else:
        returncode = child.exitstatus
    return out, returncode


class WebSettingsDashboardERPLibre(WebSettingsDashboard):

    @http.route('/web_settings_dashboard/data', type='json', auth='user')
    def web_settings_dashboard_data(self, **kw):
        res = super(WebSettingsDashboardERPLibre, self).web_settings_dashboard_data()
        if res:
            share = res.get("share")
            if share:
                try:
                    share["server_erplibre_commit"] = subprocess.check_output(["git", "describe", "--tags"]).strip()
                except:
                    print(cmdlineCall("git", ["describe", "--tags"]))
                    print("Cannot execute 'git describe --tags'")
                    share["server_erplibre_commit"] = "0".encode("utf-8")
        return res
