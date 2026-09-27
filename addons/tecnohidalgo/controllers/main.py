from odoo import http
from odoo.http import request

class TecnoHidalgoController(http.Controller):
    @http.route("/tecnohidalgo", type="http", auth="public", website=True)
    def tecnohidalgo(self, **kw):
        return request.render("tecnohidalgo.landing_page")
