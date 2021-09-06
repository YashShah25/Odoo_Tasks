from odoo import fields, models


class InheritCollage(models.Model):
    _inherit = "collage.profile"
    # _description = "This is order model"
    #
    # order_name = fields.Char(string="Product name")
    # order_id = fields.Char(string="Order ID")
