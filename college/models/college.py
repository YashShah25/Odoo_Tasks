from odoo import fields, models


class CollegeProfile(models.Model):
    _name = "college.profile"
    # _inherit = "sale.order.line"

    var_cls = fields.Char(string="var cls", store=True)


# related='product_id.name',
